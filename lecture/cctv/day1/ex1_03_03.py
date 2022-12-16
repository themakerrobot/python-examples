import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_03_01.html", {"request":request})

@app.get('/pibo', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("ex1_03_03_02.html", {"request":request, "result":"pibo"})

if __name__ == '__main__':
  uvicorn.run("ex1_03_03:app", host="0.0.0.0", port=8080)
