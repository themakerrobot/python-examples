from openpibo.speech import Dialog,Speech,Speech2
from openpibo.audio import Audio
from openpibo.device import Device
import random,time

dialog = Dialog()
speech = Speech()
speech2 = Speech2()
audio = Audio()
device = Device()

def load_dialog(filename):
  with open(filename, 'r') as f:
    return [item.split("\n")[0].split(",") for item in f.readlines()]

def get_system_message():
  res = device.send_raw("#40!")
  return res.split(":")[1].split("-")

if __name__ == "__main__":
  datas = load_dialog("record.txt")
  
  print("== Load File ==")
  print("keyword", "/" ,"Answer")
  for item in datas:
    print(item[0], "/", item[1:])

  print("== Start ==")
  while True:
    status = get_system_message()

    if 'touch' in status:
      q = input("input > ")
      #q = speech.stt()
      print("Question:", q)

      result = None
      for item in datas:
        keyword, answer = item[0], item[1:]
        if item[0] in q:
          result = random.choice(answer)
          break

      if result == None:
        result = dialog.get_dialog(q)

      print("Answer:", result)
      speech2.tts(result, filename="tts.mp3")
      audio.play("tts.mp3")
      time.sleep(1)

    time.sleep(1)
