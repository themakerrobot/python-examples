import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import base64

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_09.html", {"request":request})

@app.sio.on('image')
async def f_image(sid, msg=None):
  with open('./test.jpg', 'rb') as img:
    base64_string = base64.b64encode(img.read()).decode('utf-8')
  await app.sio.emit("image", "data:image/jpeg;charset=utf-8;base64,"+base64_string)

if __name__ == '__main__':
  uvicorn.run("ex1_03_09:app", host="0.0.0.0", port=8080)
