import cv2
import numpy as np

class TeachableMachineKeras:
  def __init__(self):
    pass

  def load(self, model_path, label_path):
    from tensorflow import keras

    with open(label_path) as f:
      c = f.read().split('\n')
      class_names = [c[i].split(maxsplit=1)[1] for i in range(len(c)-1)]

    self.model = keras.models.load_model(model_path, compile=False)
    self.class_names = class_names

  def predict(self, img):
    img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
    img = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
    img = (img / 127.5) - 1
    predictions = self.model.predict(img)[0]
    return predictions, self.class_names[np.argmax(predictions)]


if __name__ == "__main__":
    import time

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
