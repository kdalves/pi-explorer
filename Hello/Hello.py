import cv2 as cv
import numpy as np

def hello():
  caminho = "Resources/Akali.png"
  imagem = cv.imread(caminho)

  cv.imshow("Hello Imagem da Akali", imagem)
  cv.waitKey(1)

hello()