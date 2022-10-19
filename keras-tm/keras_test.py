import time
import cv2
import numpy as np

class TeachableMachineKeras:
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
    from tensorflow import keras

    with open(label_path) as f:
      c = f.read().split('\n')
      class_names = [c[i].split(maxsplit=1)[1] for i in range(len(c)-1)]

    self.model = keras.models.load_model(model_path, compile=False)
    self.class_names = class_names

  def predict(self, img):
    """
    적용한 Teachable Machine 모델을 기반으로 추론합니다.
    example::
      cm = Camera()
      img = cm.read()
      tm.predict(img)
    :param numpy.ndarray img: 이미지 객체
    :returns: 추론 결과, 가장 높은 확률을 가진 클래스 명
    """

    img = cv2.cvtColor(cv2.resize(img, (224, 224)), cv2.COLOR_BGR2RGB)
    normalized_image_array = (img.astype(np.float32) / 127.0) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    predictions = self.model.predict(data)[0]

    return predictions, self.class_names[np.argmax(predictions)]


if __name__ == "__main__":

    s = time.time()
    tk = TeachableMachineKeras()
    tk.load("keras_model.h5", "labels.txt")
    cap = cv2.VideoCapture(0)
    print("Load:", time.time()-s)
    while True:
        s = time.time()
        _, img = cap.read()
        result = tk.predict(img)
        print(time.time()-s, result)
