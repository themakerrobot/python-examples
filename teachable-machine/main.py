import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import base64
import cv2

from openpibo.vision import Camera
from tmlib import TeachableMachineKeras, TeachableMachineTf

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    img = camera.read()
    raw, res = tk.predict(img)

    img = cv2.imencode('.jpg', img)[1].tobytes()
    base64_string = base64.b64encode(img).decode('utf-8')
    return templates.TemplateResponse("index.html", {"request":request, "image":"data:image/jpeg;charset=utf-8;base64,"+base64_string, "result":str(raw) + "," +res})

@app.on_event("startup")
async def startup_event():
    global camera,tk
    camera = Camera()

    #tk = TeachableMachineKeras()
    #tk.load("./keras_model/keras_model.h5", "./keras_model/labels.txt")

    tk = TeachableMachineTf()
    tk.load("./tflite_model/model_unquant.tflite", "./tflite_model/labels.txt")

if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8080)