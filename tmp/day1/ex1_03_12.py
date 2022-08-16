import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base64
import cv2
from threading import Thread
import asyncio
from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.vision import Face


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_11.html", {"request":request})

def detect_object(img):
  items = detect.detect_object(img)
  
  for item in items:
    x1, y1, x2, y2 = item['position']
    colors = (100, 100, 200)
    camera.rectangle(img, (x1, y1), (x2, y2), colors, 1) # rectangle(img, p1, p2, colors, tickness)
    camera.putText(img, item['name'], (x1-10, y1-10), 0.6, colors, 2) # putText(img, text, points, size, colors, tickness)
  return img

def detect_face(img):
  items = face.detect(img)

  for item in items:
    x, y, w, h = item
    colors = (200,100,0)
    camera.rectangle(img, (x, y), (x+w, y+h), colors, 2) # rectangle(img, p1, p2, colors, tickness)

  return img

def my_function(img):
  return detect_face(img)
  #return detect_object(img)

def loop():
  global img
  while True:
    img = camera.read()
    img = my_function(img)
    img = cv2.imencode('.jpg', img)[1].tobytes()
    base64_string = base64.b64encode(img).decode('utf-8')
    asyncio.run(app.sio.emit("image", "data:image/jpeg;charset=utf-8;base64,"+base64_string))

@app.on_event("startup")
async def startup_event():
  global camera, detect, face
  camera = Camera()
  detect = Detect()
  face = Face()
  Thread(name='loop', target=loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("ex1_03_12:app", host="0.0.0.0", port=8080)
