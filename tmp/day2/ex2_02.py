import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base64
import cv2
import asyncio

from openpibo.vision import Camera, Face
from openpibo.motion import Motion
from threading import Thread

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex2_01.html", {"request":request})

# rectangle(img, p1, p2, colors, tickness)
def detect_face(img):
  global pos_x, pos_y
  items = face.detect(img)

  if len(items) > 0:
    x, y, w, h = items[0]
    cx, cy = int(x+w/2), int(y+h/2)
    colors = (200,100,0)
    camera.rectangle(img, (x, y), (x+w, y+h), colors, 2)
    camera.rectangle(img, (cx, cy), (cx, cy), (0,0,255), 10)
    camera.rectangle(img, (270,190), (370,290), (200,200,200), 1)
    prio_x, prio_y = pos_x, pos_y
    if cx < 270 and pos_x < 40:
      pos_x += 1
    elif cx > 370 and pos_x > -40:
      pos_x -= 1
    
    if cy < 190 and pos_y < 15:
      pos_y -= 1
    elif cy > 290 and pos_y > -15:
      pos_y += 1

    if prio_x != pos_x or prio_y != pos_y:
      motion.set_motors([0,0,-70,0, pos_x, pos_y, 0,0,70,0])
  return img

def my_function(img):
  return detect_face(img)

def loop():
  while True:
    img = camera.read()
    img = my_function(img)
    img = cv2.imencode('.jpg', img)[1].tobytes()
    base64_string = base64.b64encode(img).decode('utf-8')
    asyncio.run(app.sio.emit("stream", "data:image/jpeg;charset=utf-8;base64,"+base64_string))

@app.on_event("startup")
async def startup_event():
  global camera, face, motion, pos_x, pos_y
  camera = Camera() # 1
  face = Face()
  motion = Motion()

  pos_x, pos_y = 0, 0
  motion.set_motors([0,0,-70,0, pos_x, pos_y, 0,0,70,0])

  Thread(name='loop', target=loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("ex2_02:app", host="0.0.0.0", port=8080)
