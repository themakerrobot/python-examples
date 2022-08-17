import cv2
import openpibo_models
from PIL import Image, ImageFont, ImageDraw
import numpy as np

def putText(img, points, text, font_size, colors):
  font = ImageFont.truetype(openpibo_models.filepath("KDL.ttf"), font_size)
  # KoPub Dotum Light
  print("font_path:", openpibo_models.filepath("KDL.ttf"))
  pil = Image.fromarray(img)  # CV to PIL
  ImageDraw.Draw(pil).text(points, text, font=font, fill=colors)  # putText
  return np.array(pil)  # PIL to CV

cap = cv2.VideoCapture(0)
_, img = cap.read()

text = "가나다라마바사"
font_size = 50
points = (100, 100)
colors = (0,0,255)

img = putText(img, points, text, font_size, colors)

cv2.imwrite("test.jpg", img)
print("saved image")