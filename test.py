from openpibo.device import Device
from openpibo.vision import Detect
import time
from threading import Thread

import cv2

def dloop():
    system_check_time = time.time()
    battery_check_time = time.time()

    while True:
        if time.time() - system_check_time > 1:
            tmp = device.send_raw("#40:!").split(":")[1].split("-")
            print(tmp)
            system_check_time = time.time()
        elif time.time() - battery_check_time > 10:
            tmp = device.send_raw("#15:!").split(":")[1]
            print(tmp)
            battery_check_time = time.time()
        time.sleep(0.1)

def vloop():

    while True:
        img = cap.read()[1]
        tmp = detect.detect_object(img)
        print(tmp)

if __name__ == "__main__":
    device = Device()
    detect = Detect()
    cap = cv2.VideoCapture(0)

    Thread(name='dloop', target=dloop, args=(), daemon=True).start()
    Thread(name='vloop', target=vloop, args=(), daemon=True).start()

    while True:
        print("== main ==")
        time.sleep(1)