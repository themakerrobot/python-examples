import time
from openpibo.device import Device
from openpibo.oled import Oled

def disp_oled(b, p, t):
  oled.clear()
  oled.draw_text((0, 0), "배터리:" + b)
  oled.draw_text((0, 20), "사람:" + p)
  oled.draw_text((0, 40), "터치:" + t)
  oled.show()

def system_check():
  res = device.send_raw("#40:!").split(":")[1]
  battery = device.send_raw("#15:!").split(":")[1]
  print(res, battery)
  
  person = "O" if "person" in res else "X"
  touch = "O" if "touch" in res else "X"

  device.send_raw("#20:255,0,0!" if touch == "O" else "#20:0,0,0!")
  disp_oled(battery, person, touch)

if __name__ == "__main__":
  oled = Oled()
  device = Device()
  
  oled.set_font(size=15)

  while True:
    system_check()
    time.sleep(1)
