import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import os,base64

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)
db = []

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("mychat.html", {"request":request})

@app.sio.on('id')
async def f_message(sid):
  await app.sio.emit('id', sid)

@app.sio.on('message')
async def f_message(sid, msg=None):
  db.append(sid + ": " + msg)

  if len(db) > 10:
    db.pop(0)

  await app.sio.emit('message', db)

if __name__ == '__main__':
  uvicorn.run("mychat:app", host="0.0.0.0", port=8080)
