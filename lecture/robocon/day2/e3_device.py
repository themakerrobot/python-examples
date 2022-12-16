'''
+ 메시지 구조
 - VERSION(10) ->  ex) #10:!
 - HALT(11) -> ex) #11:!
 - DC_CONN(14) -> ex) #14:!
 - BATTERY(15) -> ex) #15:!
 - NEOPIXEL(20) -> ex) #20:255,255,255!
 - NEOPIXEL_EACH(23) -> ex) #23:255,255,255,255,255,255!
 - SYSTEM(40) -> ex) #40:! -> PIR-TOUCH-DC-BUTTON-...
'''

from openpibo.device import Device

def send_device(cmd):
  return device.send_raw(cmd)

if __name__ == "__main__":
  device = Device()
  
  pkt = {"opcode": "20", "data": "255,0,0"}
  #pkt = {"opcode": "23", "data": "255,0,0,0,0,255"}
  #pkt = {"opcode": "14", "data": ""}
  #pkt = {"opcode": "15", "data": ""}
  #pkt = {"opcode": "40", "data": ""}

  print('Send:', pkt["opcode"], pkt["data"])        # 실행한 명령어 출력
  result = send_device(f'#{pkt["opcode"]}:{pkt["data"]}!')
  print('Receive:', result)             # Device로부터 받은 응답 출력
