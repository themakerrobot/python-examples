import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base64
import cv2
import asyncio

from openpibo.vision import Camera, Detect, Face, TeachableMachine
from threading import Thread

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex2_01.html", {"request":request})

# 1
def basic(img):
  #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #camera.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 1)
  #camera.putText(img, "Hello vision", (200, 200), 0.6, (0, 255, 0), 2)
  #cv2.circle(img, (320, 240), 50, (0, 0, 255), 3)
  return img

# 2
# rectangle(img, p1, p2, colors, tickness)
def detect_face(img):
  items = face.detect(img)

  for item in items:
    x, y, w, h = item
    colors = (200,100,0)
    camera.rectangle(img, (x, y), (x+w, y+h), colors, 2)
  return img

# 3
# putText(img, text, points, size, colors, tickness)
def detect_object(img):
  items = detect.detect_object(img)

  for item in items:
    x1, y1, x2, y2 = item['position']
    colors = (100, 100, 200)
    camera.rectangle(img, (x1, y1), (x2, y2), colors, 1)
    camera.putText(img, item['name'], (x1-10, y1-10), 0.6, colors, 2)
  return img

# 4
def classify_from_tm(img):
  res, raw = tm.predict(img)
  colors = (200, 200, 200)
  camera.putText(img, "{} : {:.2f}%".format(res, raw.max()*100), (50, 50), 0.5, colors, 2)

  for i in range(len(tm.class_names)):
    camera.putText(img, "{}:{:.2f}%".format(tm.class_names[i], raw[i]*100), (50, 50+((i+1)*20)), 0.5, colors, 1)
  return img


def my_function(img):
  return basic(img)  # 1
  #return detect_face(img) # 2
  #return detect_object(img) # 3
  #return classify_from_tm(img) # 4

def loop():
  while True:
    img = camera.read()
    img = my_function(img)
    img = cv2.imencode('.jpg', img)[1].tobytes()
    base64_string = base64.b64encode(img).decode('utf-8')
    asyncio.run(app.sio.emit("stream", "data:image/jpeg;charset=utf-8;base64,"+base64_string))

@app.on_event("startup")
async def startup_event():
  global camera, detect, face, tm
  camera = Camera() # 1
  face = Face() # 2
  detect = Detect() # 3
  # 4
  tm = TeachableMachine()
  tm.load("./model_unquant.tflite", "./labels.txt")
  
  Thread(name='loop', target=loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("ex2_01:app", host="0.0.0.0", port=8080)