import uvicorn
from fastapi import FastAPI
from queue import Queue
from threading import Thread
import serial
import time
import os
from urllib import parse

app = FastAPI()

def send_raw(raw):
  dev.write(raw.encode('utf-8'))
  time.sleep(0.05)

  data = ""
  while True:
    ch = dev.read().decode()
    if ch == '#' or ch == '\r' or ch == '\n':
      continue
    if ch == '!':
      break
    data += ch
  return data

def decode(pkt):
  global pir, touch, dc, button, battery
  opcode, data = [item for item in pkt.split(":")] 

  if opcode == "40":
    pir, touch, dc, button, _, _ = [item for item in data.split("-")]
  if opcode == "15":
    battery = data

def device_loop():
  global q
  system_check_time = time.time()
  battery_check_time = time.time()

  while True:
    if time.time() - system_check_time > 1:
      decode(send_raw("#40:!"))
      system_check_time = time.time()
    elif time.time() - battery_check_time > 10:
      decode(send_raw("#15:!"))
      battery_check_time = time.time()
    elif q.qsize() > 0:
      data = send_raw(q.get())
    time.sleep(0.1)

@app.get("/device/{opcode}/{data}")
async def f_device(opcode, data):
  global q
  q.put(f"#{opcode}:{data}!")
  return {"result":"ok", "data":{"opcode":opcode, "data":data}}

@app.get("/system")
async def f_system():
  return {"result":"ok", "data":{"pir":pir, "touch":touch, "dc":dc, "button":button, "battery":battery}}

@app.get("/servo/{data}")
async def f_servo(data):
  os.system(data)  
  return {"result":"ok", "data":data}

@app.on_event("startup")
async def startup_event():
  global dev, q, pir, touch, dc, button, battery
  pir = ""
  touch = ""
  dc = ""
  button = ""
  battery = ""
  dev = serial.Serial(port="/dev/ttyS0", baudrate=9600)
  q = Queue()
  Thread(name='device_loop', target=device_loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8080)
