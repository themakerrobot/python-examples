import requests
import time

motor_cmds = ['servo move 0 0 -500 0 -300 0 0 0 500 0 500', 'servo move 0 0 500 0 300 0 0 0 -500 0 0 500', 'servo move 0 0 0 0 0 0 0 0 0 0 500']
eye_cmds = ['255,0,0,255,0,0', '0,255,0,0,255,0', '0,0,255,0,0,255']
idx = 0

while True:
  res = requests.get(f"http://0.0.0.0:8080/system").json()
  res = requests.get(f"http://0.0.0.0:8080/servo/{motor_cmds[idx]}").json()
  res = requests.get(f"http://0.0.0.0:8080/device/23/{eye_cmds[idx]}").json()
  idx = 0 if idx == 2 else idx+1
  time.sleep(0.5)
