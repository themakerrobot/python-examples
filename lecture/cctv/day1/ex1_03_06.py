import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import base64
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  os.system('raspistill -t 100 -vf -hf -w 640 -h 480 -o /home/pi/test.jpg')
  with open('/home/pi/test.jpg', 'rb') as img:
    base64_string = base64.b64encode(img.read()).decode('utf-8')
  return templates.TemplateResponse("ex1_03_06.html", {"request":request, "result":"data:image/jpeg;charset=utf-8;base64,"+base64_string})

if __name__ == '__main__':
  uvicorn.run("ex1_03_06:app", host="0.0.0.0", port=8080)
