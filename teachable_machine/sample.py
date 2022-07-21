import time
from tflite_runtime.interpreter import Interpreter
import cv2
import numpy as np
from PIL import Image

class TeachableMachine:
  """
Functions:
:meth:`~openpibo.vision.TeachableMachine.load`
:meth:`~openpibo.vision.TeachableMachine.predict`

  파이보의 카메라 Teachable Machine 기능을 사용합니다.

  * ``이미지 프로젝트``의 ``표준 이미지 모델``을 사용합니다.
  * ``Teachable Machine``에서 학습한 모델을 적용하여 추론할 수 있습니다.

  example::

    from openpibo.vision import TeachableMachine

    tm = TeachableMachine()
    # 아래의 모든 예제 이전에 위 코드를 먼저 사용합니다.
  """

  def __init__(self):
    pass

  def load(self, model_path, label_path):
    """
    Teachable Machine 모델을 초기화 합니다.

    example::

      tm.load('model_keras.h5', 'labels.txt')

    :param str model_path: Teachable Machine에서 학습한 모델 파일

    :param str label_path: Teachable Machine에서 학습한 라벨 파일
    """
    with open(label_path, 'r') as f:
      c = f.readlines()
      class_names = [c[i].split(maxsplit=1)[1] for i in range(len(c)-1)]

    # Load TFLite model and allocate tensors
    self.interpreter = Interpreter(model_path=model_path)
    self.interpreter.allocate_tensors()

    # Get input and output tensors.
    self.input_details = self.interpreter.get_input_details()
    self.output_details = self.interpreter.get_output_details()

    # check the type of the input tensor
    self.floating_model = self.input_details[0]['dtype'] == np.float32

    self.height = self.input_details[0]['shape'][1]
    self.width = self.input_details[0]['shape'][2]

    self.class_names = class_names

  def predict(self, img):
    """
    적용한 Teachable Machine 모델을 기반으로 추론합니

    example::

      cm = Camera()
      img = cm.read()
      tm.predict(img)

    :param numpy.ndarray img: 이미지 객체

    :returns: 추론 결과, 가장 높은 확률을 가진 클래스 명
    """

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (self.width, self.height))
    image = Image.fromarray(img)

    # Add a batch dimension
    input_data = np.expand_dims(image, axis=0)

    if self.floating_model:
      input_data = (np.float32(input_data) - 127.5) / 127.5

    # feed data to input tensor and run the interpreter
    self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
    self.interpreter.invoke()

    # Obtain results and map them to the classes
    preds = self.interpreter.get_tensor(self.output_details[0]['index'])
    preds = np.squeeze(preds)
    return preds, self.class_names[np.argmax(preds)]

if __name__ == "__main__":
  s = time.time()
  tk = TeachableMachine()
  tk.load("../../model_unquant.tflite", "labels.txt")
  cap = cv2.VideoCapture(0)
  print("Load:", time.time()-s)
  while True:
    s = time.time()
    _, img = cap.read()
    result = tk.predict(img)
    print(time.time()-s, result)
