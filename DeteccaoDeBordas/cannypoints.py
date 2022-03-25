import cv2
import numpy as np
from copy import copy
import random

STEP = 5
JITTER = 3
RADIUS = 2

T1 = 10
edges = 0

caminho = 'Resources/deteccao_de_bordas/shoto-todoroki1.jpg'
imagem = cv2.imread(caminho, 0)

def main():
  if imagem is not None:
    height, width = imagem.shape
    points = copy(imagem)

    for i in range(height):
      for j in range(width):
        points[i, j] = 255

    xrange = np.zeros(int(height/STEP))
    yrange = np.zeros(int(width/STEP))

    for xvalue in range(len(xrange)):
      xrange[xvalue] = xvalue

    for yvalue in range(len(yrange)):
      yrange[yvalue] = yvalue

    xrange = [value*STEP+STEP/2 for value in xrange]
    yrange= [value*STEP+STEP/2 for value in yrange]

    np.random.shuffle(xrange)

    for i in xrange:
      np.random.shuffle(yrange)
      for j in yrange:
        x = int(i + random.randint(1, 2*JITTER-JITTER))
        y = int(j + random.randint(1, 2*JITTER-JITTER))
        if(x >= height):
          x = height-1
        if( y >= width):
          y = width-1
        gray = imagem[x,y]
        cv2.circle(points, (y, x), RADIUS, int(gray), -1, cv2.LINE_AA)

    edges = cv2.Canny(points, T1, 3*T1) 

    for i in range(height):
      for j in range(width):
        if(edges[i, j] != 0):
          gray = imagem[i,j]
          cv2.circle(points, (j, i), RADIUS, int(gray), -1, cv2.LINE_AA)

    cv2.imshow("cannypoint", points)
    cv2.imwrite("cannypoint.png", points)
    cv2.waitKey(0)     
    cv2.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

if __name__ == '__main__':
  main()
