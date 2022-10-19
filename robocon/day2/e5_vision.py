from openpibo.vision import Camera,Face,Detect,TeachableMachine

def run_camera():
  img = camera.read() 
  #img = camera.read("/home/pi/openpibo-files/image/bus.jpg")
  #print(img)
  
  camera.rectangle(img,  (100, 100), (300, 300), (0,0,255), 1) # p1, p2, colors, tickness
  camera.circle(img,  (100, 100), 100, (0,255,0), 1) # p, r, colors, tickness
  camera.putText(img, "Hello Camera", (50, 50), 1, (255,0,0), 1) # text, p, size, colors, tickness

  import cv2ko
  img = cv2ko.putText(img, "안녕하세요", (300, 300), 50, (255,0,0)) # img, point, text, size, colors

  camera.imwrite("result.jpg", img)

def detect_face():
  face = Face()
  img = camera.read() 
  items = face.detect(img)
  print("Faces:", len(items))

  if len(items) > 0:
    for item in items:
      res = face.get_ageGender(img, item)
      print(item, res)

  #camera.imwrite("result.jpg", img)

def detect_object():
  detect = Detect()

  img = camera.read()

  res = detect.detect_object(img.copy())
  print("Object:", res)
  res = detect.detect_qr(img.copy())
  print("QR:", res)


def detect_from_tm():
  tm = TeachableMachine()
  
  img = camera.read()
  
  tm.load("model_unquant.tflite", "labels.txt")
  res = tm.predict(img)
  print(res)


if __name__ == "__main__":
  camera = Camera()
  run_camera()
  #detect_face()
  #detect_object()
  #detect_from_tm()
