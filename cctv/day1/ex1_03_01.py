import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 1) 기본 서버
@app.get("/")
async def root():
    return "Hello fastapi"
    #return {"Hello": "fastapi"}

# 2) 라우팅
@app.get("/hi")
async def hi():
  return "Hi pibo" 

@app.get("/bye")
async def bye():
  return "Bye pibo" 

# 3) get 방식 파라미터 전달하기
@app.get("/register/{name}")
async def register(name, age=None, gender=None):
  return {"name":name, "age":age, "gender":gender}

if __name__ == '__main__':
  uvicorn.run("ex1_03_01:app", host="0.0.0.0", port=8080)
