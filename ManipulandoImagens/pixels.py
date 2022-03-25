import cv2 as cv
import numpy as np

def pixels():
  caminho = "Resources/bolhas.png"
  imagem = cv.imread(caminho, cv.IMREAD_GRAYSCALE)
  
  if imagem is not None:
    cv.namedWindow("Janela", cv.WINDOW_AUTOSIZE)

    for i in range(200, 211):
      for j in range(10,200):
        imagem[i,j] = 0

    cv.imshow("Janela", imagem)   
    cv.waitKey()

    imagem_rgb = cv.imread(caminho, cv.IMREAD_COLOR)

    vetor = np.array(imagem_rgb)

    vetor[0] = imagem[i,j,0] #Blue
    vetor[1] = imagem[i,j,0] # Green
    vetor[2] = imagem[i,j,255] #Red

    for i in range(200, 211):
      for j in range(10,200):
        imagem[i,j] = vetor

    cv.imshow("Janela", imagem)   
    cv.waitKey(0)
    cv.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

pixels()