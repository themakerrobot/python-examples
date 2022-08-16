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
  return templates.TemplateResponse("ex2_02.html", {"request":request})

@app.sio.on('train')
async def f_train(sid, d=None):
  frame = img.copy()
  res = face.detect(frame)
  
  if len(res) > 0:
    face.train_face(frame, res[0], d)
    face.save_db("./facedb")
    x, y, w, h = res[0]
    colors = (200,100,0)
    camera.rectangle(frame, (x, y), (x+w, y+h), colors, 2) # rectangle(img, p1, p2, colors, tickness)
    camera.putText(frame, d, (x-10, y-10), 0.6, colors, 2)
    frame = cv2.imencode('.jpg', frame)[1].tobytes()
    base64_string = base64.b64encode(frame).decode('utf-8')
    await app.sio.emit("res", "data:image/jpeg;charset=utf-8;base64,"+base64_string)

def my_function(frame):
  items = face.detect(frame)

  if len(items) > 0:
    x, y, w, h = items[0]
    colors = (200,100,0)
    camera.rectangle(frame, (x, y), (x+w, y+h), colors, 2) # rectangle(img, p1, p2, colors, tickness)
    res = face.recognize(frame, items[0])
    if res == False:
      res = {'name':'Guest', 'score':0}
    camera.putText(frame, res["name"], (x-10, y-10), 0.6, colors, 2)
  return frame


def loop():
  global img
  while True:
    img = camera.read()
    frame = my_function(img.copy())
    frame = cv2.imencode('.jpg', frame)[1].tobytes()
    base64_string = base64.b64encode(frame).decode('utf-8')
    asyncio.run(app.sio.emit("image", "data:image/jpeg;charset=utf-8;base64,"+base64_string))

@app.on_event("startup")
async def startup_event():
  global camera, face
  camera = Camera()
  face = Face()
  try:
    face.load_db("./facedb")
  except Exception as ex:
    print(ex)
  Thread(name='loop', target=loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("ex2_02:app", host="0.0.0.0", port=8080)
