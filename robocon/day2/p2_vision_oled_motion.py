import time
from openpibo.vision import Camera,Face
from openpibo.oled import Oled
from openpibo.motion import Motion

pos_x,pos_y = 0,0

def disp_oled(img):
  d = camera.convert_img(img, w=128, h=64)
  oled.draw_data(d)
  oled.show()

def disp_face(img):
  global pos_x,pos_y
  
  items = face.detect(img)
  for item in items:
    x,y,w,h = item
    camera.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 10)
  
  # tracking face0
  if len(items) > 0:
    x, y, w, h = items[0]
    cx, cy = int(x+w/2), int(y+h/2)
    camera.rectangle(img, (cx, cy), (cx, cy), (0,0,0), 50)
    prio_x, prio_y = pos_x, pos_y

    if cx < 270 and pos_x < 40:
      pos_x += 1
    elif cx > 370 and pos_x > -40:
      pos_x -= 1
    
    if cy > 290 and pos_y < 15:
      pos_y += 1
    elif cy < 190 and pos_y > -15:
      pos_y -= 1

    if prio_x != pos_x or prio_y != pos_y:
      motion.set_motors([0,0,-70,0, pos_x, pos_y, 0,0,70,0])
  return img

if __name__ == "__main__":
  oled = Oled()
  camera = Camera()
  face = Face()
  motion = Motion()

  while True:
    img = camera.read()
    img = disp_face(img)
    disp_oled(img)