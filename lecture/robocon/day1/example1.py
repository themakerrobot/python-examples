import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 1) 기본 서버
@app.get("/")
async def root():
    return "Hi fastapi"
    #return {"Hello": "fastapi"}

# 2) 라우팅
@app.get("/api2")
async def hi():
  return "Hello fastapi" 

# 3) get 방식 파라미터 전달하기
@app.get("/api3/{name}")
async def register(name, age=None, gender=None):
  return {"name":name, "age":age, "gender":gender}

# 4) HTML 응답
from fastapi.responses import HTMLResponse
@app.get("/api4/{name}", response_class=HTMLResponse)
async def register(name):
    return f"<h1>Hello Fastapi, I'm {name}</h1>"

# 5) HTML 파일 분리
from fastapi import Request
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
@app.get('/api5', response_class=HTMLResponse)
async def main(request: Request):
  return templates.TemplateResponse("example1.html", {"request":request, "result": "Hello World"})

if __name__ == '__main__':
  uvicorn.run("example1:app", host="0.0.0.0", port=8080)
