import time
from openpibo.oled import Oled

# (0,0), (0,20)에 15 크기의 text 표시
def text():
  oled.clear()                              # 화면 지우기
  oled.set_font(size=15)
  oled.draw_text((0, 0), "안녕? 난 파이보야 ")  # (0,0)에 문자열 출력
  oled.draw_text((0,20), "☆  ★ ") # (0,20)에 문자열 출력
  oled.show() # 화면에 표시

def image():
  PATH = "/home/pi/openpibo-files/icon/"
  oled.clear()                              # 화면 지우기
  oled.draw_image(PATH + "/pibo_logo.png")  # 이미지 그리기
  oled.show()   # 화면에 표시

def figure():
  oled.clear()                              # 화면 지우기
  oled.draw_rectangle((10,10,30,30), True)  # 길이가 20인 채워진 사각형 그리기
  oled.draw_ellipse((70,40,90,60), False)   # 지름이 20인 빈 원 그리기
  oled.draw_line((15,15,80,50))             # 선 그리기
  oled.show()                               # 화면에 표시

if __name__ == "__main__":
  oled = Oled()
  #text()
  #image()
  #figure()
