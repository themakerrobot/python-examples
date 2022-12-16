import uvicorn
from fastapi_socketio import SocketManager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
socketio = SocketManager(app=app)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_08.html", {"request":request})

@app.sio.on('message')
async def f_message(sid, msg=None):
  await app.sio.emit('message', "Your Message: " + msg)

if __name__ == '__main__':
  uvicorn.run("ex1_03_08:app", host="0.0.0.0", port=8080)
