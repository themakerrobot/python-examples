import time

from openpibo.motion import Motion
from openpibo.device import Device

def run():
  o = Motion()
  d = Device()

  while True:
    d.send_raw("#20:255,255,0!")
    pos = [0,0,30,20, 30,0, 0,0,30,20]
    o.set_motors(positions=pos, movetime=1000)
    time.sleep(1.1)
    
    
    
    d.send_raw("#20:0,255,255!")
    pos = [0,0,-30,-20, -30,0, 0,0,-30,-20]
    o.set_motors(positions=pos, movetime=1000)
    time.sleep(1.1)    

if __name__ == "__main__":
  run()
