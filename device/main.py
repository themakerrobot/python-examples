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
    if ch in ['#','\r','\n']:
      continue
    if ch == '!':
      break
    data += ch
  return data

def device_loop():
  global q, system_data, battery_data
  system_check_time = time.time()
  battery_check_time = time.time()

  while True:
    if time.time() - system_check_time > 1:
      system_data = send_raw("#40:!")
      system_check_time = time.time()
    elif time.time() - battery_check_time > 10:
      battery_data = send_raw("#15:!")
      battery_check_time = time.time()
    elif q.qsize() > 0:
      data = send_raw(q.get())
    time.sleep(0.1)

@app.get("/device/{pkt}")
async def f_device(pkt):
  global q
  opcode, data = [item for item in pkt.split(":")] 
  
  if opcode == "40":
    return {"result":"ok", "data":system_data}
  elif opcode == "15":
    return {"result":"ok", "data":battery_data}
  else:
    q.put(f"#{pkt}!")
    return {"result":"ok", "data":"ok"}

@app.get("/servo/{data}")
async def f_servo(data):
  os.system(data)  
  return {"result":"ok", "data":data}

@app.on_event("startup")
async def startup_event():
  global dev, q, system_data, battery_data
  system_data = "------"
  battery_data = "0%"

  dev = serial.Serial(port="/dev/ttyS0", baudrate=9600)
  q = Queue()
  Thread(name='device_loop', target=device_loop, args=(), daemon=True).start()

if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8080)
