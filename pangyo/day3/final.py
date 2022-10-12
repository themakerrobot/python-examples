import uvicorn

from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from threading import Thread
from datetime import datetime

import base64
import cv2
import asyncio

from openpibo.vision import Camera,Detect,Face
from openpibo.motion import Motion

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("final.html", {"request":request})

@app.sio.on('control')
async def f_control(sid, d=None):
  global pos_x, pos_y

  cur_x, cur_y = pos_x, pos_y
  if d == "down":
    pos_y = pos_y + 1 if pos_y < 15 else pos_y 
  elif d == "up":
    pos_y = pos_y - 1 if pos_y > -15 else pos_y 
  elif d == "left":
    pos_x = pos_x + 1 if pos_x < 40 else pos_x 
  elif d == "right":
    pos_x = pos_x - 1 if pos_x > -40 else pos_x 

  if cur_x != pos_x or cur_y != pos_y:
    motion.set_motors([0,0,-80,0, pos_x, pos_y, 0,0,80,0])

  await app.sio.emit("position", {"x": pos_x, "y": pos_y})

def detect_items(img):
  face_items = face.detect(img)
  object_items = detect.detect_object(img)

  for item in face_items:
    x, y, w, h = item
    colors = (150,50,50)
    cv2.circle(img, (int(x+w/2), int(y+h/2)), int((w+h)/4), colors, 2) # r= (w/2 + h/2 ) /2
    res = face.get_ageGender(img, item)
    camera.putText(img, res['gender'] + res['age'], (x-10, y-10), 0.6, colors,2)

  for item in object_items:
    x1, y1, x2, y2 = item['position']
    colors = (50,50,150)
    camera.rectangle(img, (x1, y1), (x2, y2), colors, 1)
    camera.putText(img, item['name'], (x1-10, y1-10), 0.6, colors, 2)
  
  camera.putText(img, str(datetime.now()).split(".")[0], (5, 20), 0.5, (0,0,0), 2)
  return img

def loop():
  while True:
    img = camera.read()
    img = detect_items(img)
    img = cv2.imencode('.jpg', img)[1].tobytes()
    base64_string = base64.b64encode(img).decode('utf-8')
    asyncio.run(app.sio.emit("stream", "data:image/jpeg;charset=utf-8;base64,"+base64_string))

@app.on_event("startup")
async def startup_event():
  global camera,detect,face,motion, pos_x,pos_y
  camera = Camera()
  face = Face()
  detect = Detect()
  motion = Motion()

  pos_x, pos_y = 0, 0
  motion.set_motors([0,0,-80,0, pos_x, pos_y, 0,0,80,0])
  Thread(name='loop', target=loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("final:app", host="0.0.0.0", port=8080)
