import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse("<h1>Hello Fastapi</h1>")

@app.get("/hi/{name}")
async def register(name):
    return HTMLResponse(f"<h1>Hello Fastapi, I'm {name}</h1>")

if __name__ == '__main__':
  uvicorn.run("ex1_03_02:app", host="0.0.0.0", port=8080)
