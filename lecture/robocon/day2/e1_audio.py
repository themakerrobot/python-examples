import time
from openpibo.audio import Audio

PATH = "/home/pi/openpibo-files/audio"

# test.mp3 파일 5초 재생 후 정지
def play():
  audio.play(filename=PATH + "/opening.mp3", volume=60)
  time.sleep(2) # 2초동안 프로세스 정지
  audio.stop()

if __name__ == "__main__":
  audio = Audio()
  play()