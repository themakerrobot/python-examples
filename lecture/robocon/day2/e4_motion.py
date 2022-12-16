import time,random
from openpibo.motion import Motion

def run_motor():
  while True:
    motion.set_motors(positions=[0,0,30,20, 30,0, 0,0,30,20], movetime=1400)
    time.sleep(2)
    motion.set_motors(positions=[0,0,-30,-20, -30,0, 0,0,-30,-20], movetime=700)
    time.sleep(2)

def run_motion():
  motions = motion.get_motion()
  name = random.choice(motions)

  print(f"Motions: {motions}\n")
  print(f"Motion name: {name}\n")
  print(f"Motion pos: {motion.get_motion(name)}")

  motion.set_motion(name=name, cycle=3)

if __name__ == "__main__":
  motion = Motion()
  run_motor()
  #run_motion()
