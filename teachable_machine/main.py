from importlib import import_module
import os
from flask import Flask, render_template, Response
from teachable import TeachableMachine
import cv2

app = Flask(__name__)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

o = TeachableMachine()

@app.route('/')
def index():
  """Video streaming home page."""
  return render_template('index.html')

def MyFunction(img):
  res, raw = o.predict(img)
  cv2.putText(img, "{} : {:.2f}%".format(res, raw.max()*100), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

  for i in range(len(o.class_names)):
    cv2.putText(img, "{}:{:.2f}%".format(o.class_names[i], raw[i]*100), (50, 50+((i+1)*20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
  return img

def gen():
  """Video streaming generator function."""
  yield b'--frame\r\n'
  o.load("./model_unquant.tflite", "./labels.txt")
  while True:
      cap.grab()
      cap.grab()
      frame = cap.read()[1]
      frame = MyFunction(frame)
      frame = cv2.imencode(".jpg", frame)[1]
      frame = frame.tobytes()
      yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
  """Video streaming route. Put this in the src attribute of an img tag."""
  return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
  app.run(host='0.0.0.0', threaded=True)
