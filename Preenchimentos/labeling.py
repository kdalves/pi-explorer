import cv2 as cv
import numpy as np

def labelling():
  caminho = "Resources/bolhas.png"
  imagem = cv.imread(caminho)

  if imagem is not None:
    imagem = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

    (width, height) = imagem.shape[:2]

    nobjetos = 0
    
    mascara = np.zeros((height + 2, width + 2), np.uint8)

    for i in range(0, height):
      for j in range(0, width):
        if imagem[i,j] == 255:
          #achou um objeto
          nobjetos = nobjetos + 1

          # preenche o objeto com o contador
          cv.floodFill(imagem, mascara, (j,i), nobjetos)

    print('width: ', width)
    print('height: ', height)

    # Numero de objetos está errado. Conta pixels 255 e não as bolhas em si
    print('Total de bolhas: ', nobjetos)

    realce = cv.equalizeHist(imagem)
    cv.imshow('Imagem', imagem)
    cv.imshow('Realce', realce)
    cv.imwrite("labeling.png", imagem)

    cv.waitKey(0)
    cv.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

labelling()
