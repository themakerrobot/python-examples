import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_07.html", {"request":request})

@app.sio.on('time')
async def f_message(sid, msg=None):
  await app.sio.emit('time', str(datetime.now()))

if __name__ == '__main__':
  uvicorn.run("ex1_03_07:app", host="0.0.0.0", port=8080)
