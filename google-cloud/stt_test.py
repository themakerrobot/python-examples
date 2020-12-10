from sttlib import Stt

O = Stt("/home/pi/piboproject-d783ed0496cb.json")
O.record()
ret = O.getText(lang="en-US")
print(ret)
