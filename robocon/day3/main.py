import uvicorn,cv2,base64,asyncio,time

from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from threading import Thread
from datetime import datetime
from queue import Queue

from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.oled import Oled
from openpibo.vision import Camera,Detect

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

g_m4_pos,g_m5_pos,N = 0,0,999
g_system = {"battery":"-", "plug":"-", "pir":"-", "touch":"-", "button":"-"}

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("index.html", {"request":request})

# motion
@app.sio.on('set_motion')
async def set_motion(sid, name="stop"):
  motion.set_motion(name=name)

@app.sio.on('set_motor')
async def set_motor(sid, value=[0, 0]):
  global g_m4_pos, g_m5_pos

  g_m4_pos += value[0]
  g_m5_pos += value[1]

  g_m4_pos = 35 if g_m4_pos > 35 else g_m4_pos
  g_m4_pos = -35 if g_m4_pos < -35 else g_m4_pos

  g_m5_pos = 15 if g_m5_pos > 15 else g_m5_pos
  g_m5_pos = -15 if g_m5_pos < -15 else g_m5_pos

  motion.set_motors([N,N,N,N, g_m4_pos, g_m5_pos, N,N,N,N])
  await app.sio.emit("m_head_value", [g_m4_pos, g_m5_pos])

@app.sio.on('head_value')
async def set_motor(sid):
  await app.sio.emit("m_head_value", [g_m4_pos, g_m5_pos])

# device
def dloop():
  global queue,g_system
  system_check_time = time.time()
  battery_check_time = time.time()

  while True:
    if time.time() - system_check_time > 1:
      tmp = device.send_raw("#40:!").split(":")[1].split("-")
      g_system["pir"] = tmp[0] if tmp[0] != "" else g_system["pir"]
      g_system["touch"] = "on" if tmp[1] == "touch" else "off"
      g_system["plug"] = tmp[2] if tmp[2] != "" else g_system["plug"]
      g_system["button"] = "on" if tmp[3] == "on" else "off"

      asyncio.run(app.sio.emit("device", g_system))
      system_check_time = time.time()
    elif time.time() - battery_check_time > 10:
      g_system["battery"] = device.send_raw("#15:!").split(":")[1]
      battery_check_time = time.time()
    elif queue.qsize() > 0:
      device.send_raw(queue.get())
    else:
      pass
    time.sleep(0.1)

@app.sio.on('set_oled')
async def set_oled(sid, text=""):
  oled.clear()
  oled.draw_text((0,10), text)
  oled.draw_line((0,40,128,40))
  oled.show()

@app.sio.on('set_led')
async def set_led(sid, value="0,0,0,0,0,0"):
  global queue
  queue.put(f"#23:{value}!")


# vision
def detect_items(img):
  object_items = detect.detect_object(img)

  for item in object_items:
    x1, y1, x2, y2 = item['position']
    colors = (50,50,150)
    camera.rectangle(img, (x1, y1), (x2, y2), colors, 1)
    camera.putText(img, item['name'], (x1-10, y1-10), 0.6, colors, 2)

  camera.putText(img, str(datetime.now()).split(".")[0], (5, 20), 0.7, (0,0,0), 2)
  return img, [item['name'] for item in object_items]

def vloop():
  while True:
    img = camera.read()
    img, result = detect_items(img)
    img = cv2.resize(img, (320,240))
    img = cv2.imencode('.jpg', img)[1].tobytes()
    base64_string = base64.b64encode(img).decode('utf-8')
    asyncio.run(app.sio.emit("vision", {"result":result ,"image":"data:image/jpeg;charset=utf-8;base64,"+base64_string}))
    time.sleep(1)


@app.on_event("startup")
async def startup_event():
  global motion,oled,device,camera,detect,queue
  motion = Motion()
  oled = Oled()
  device = Device()
  camera = Camera()
  detect = Detect()
  queue = Queue()
  device.send_raw("#30:on!")
  g_system["plug"] = device.send_raw("#14:!").split(":")[1]

  oled.set_font(size=20)
  motion.set_motors([N,N,N,N, g_m4_pos, g_m5_pos, N,N,N,N])

  Thread(name='vloop', target=vloop, args=(), daemon=True).start()
  Thread(name='dloop', target=dloop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8080)