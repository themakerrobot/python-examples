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
from openpibo.vision import TeachableMachine


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_11.html", {"request":request})

def my_function(img):
  res, raw = tm.predict(img)
  camera.putText(img, "{} : {:.2f}%".format(res, raw.max()*100), (50, 50), 0.5, (255,255,255), 2)

  for i in range(len(tm.class_names)):
    camera.putText(img, "{}:{:.2f}%".format(tm.class_names[i], raw[i]*100), (50, 50+((i+1)*20)), 0.5, (255,255,255), 1)
  return img


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
  global camera, tm
  camera = Camera()
  tm = TeachableMachine()
  tm.load("./model_unquant.tflite", "./labels.txt")
  Thread(name='loop', target=loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("ex1_03_13:app", host="0.0.0.0", port=8080)
