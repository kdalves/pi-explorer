import cv2 as cv
import numpy as np

def labelling():
  caminho = "Resources/muitos_objetos_bolhas.png"
  # caminho = "Resources/dobro_tamanho_bolhas.png"
  imagem = cv.imread(caminho)
  erro = False

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

          if nobjetos <= 255:
            # preenche o objeto com o contador
            cv.floodFill(imagem, mascara, (j,i), nobjetos)
          else:  
            erro = True

    if erro is not True:
      print('width: ', width)
      print('height: ', height)

      # Numero de objetos está errado. Conta pixels 255 e não as bolhas em si
      print('Total de bolhas: ', nobjetos)

      realce = cv.equalizeHist(imagem)
      cv.imshow('Imagem', imagem)
      cv.imshow('Realce', realce)
      cv.imwrite("doble_labeling.png", imagem)
    else:
      print('Imagem possui mais de 255 objetos, dificulta a rotulacao. Por favor selecione outra imagem com menos objetos.')

    cv.waitKey(0)
    cv.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

labelling()
