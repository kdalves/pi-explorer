import cv2 as cv
import numpy as np

def labelling():
  caminho = "Resources/bolhas.png"
  imagem = cv.imread(caminho)

  if imagem is not None:
    # imagem = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
    #inverso da cor
    imagem = 255 - imagem

    (width, height) = imagem.shape[:2]

    nobjetos = 0
    
    mascara = np.zeros((height + 2, width + 2), np.uint8)

    # Aprimore o algoritmo de contagem apresentado para identificar regiões com ou sem buracos internos que existam na cena.
    #  Assuma que objetos com mais de um buraco podem existir. 
    # Inclua suporte no seu algoritmo para não contar bolhas que tocam as bordas da imagem.
    #  Não se pode presumir, a priori, que elas tenham buracos ou não.
    for i in range(0, height):
      for j in range(0, width):
        if any(imagem[i,j] == [255,255,255]):
        #   print(imagem[i,j])
          #achou um objeto
          nobjetos = nobjetos + 1

          # preenche o objeto com o contador
          cv.floodFill(imagem, mascara, (0,0), nobjetos)

    print('width: ', width)
    print('height: ', height)

    # Numero de objetos está errado. Conta pixels 255 e não as bolhas em si
    # print('Total de bolhas: ', nobjetos)

    # realce = cv.equalizeHist(imagem)
    cv.imshow('Imagem', imagem)
    # cv.imshow('Realce', realce)
    # cv.imwrite("labeling.png", imagem)

    

    # Threshold.
    # Set values equal to or above 220 to 0.
    # Set values below 220 to 255.

    # th, im_th = cv.threshold(imagem, 220, 255, cv.THRESH_BINARY_INV)

    # # Copy the thresholded image.
    # im_floodfill = im_th.copy()

    # # Mask used to flood filling.
    # # Notice the size needs to be 2 pixels than the image.
    # h, w = im_th.shape[:2]
    # mask = np.zeros((h+2, w+2), np.uint8)

    # # Floodfill from point (0, 0)
    # cv.floodFill(im_floodfill, mask, (0,0), 255)


    # # Invert floodfilled image
    # im_floodfill_inv = cv.bitwise_not(im_floodfill)

    # # Combine the two images to get the foreground.
    # im_out = im_th | im_floodfill_inv

    # # Display images.
    # cv.imshow("Thresholded Image", im_th)
    # cv.imshow("Floodfilled Image", im_floodfill)
    # cv.imshow("Inverted Floodfilled Image", im_floodfill_inv)
    # cv.imshow("Foreground", im_out)


    cv.waitKey(0)
    cv.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

labelling()
