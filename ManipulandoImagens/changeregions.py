import cv2 as cv

def concat_tile(im_list_2d):
    return cv.vconcat([cv.hconcat(im_list_h) for im_list_h in im_list_2d])


def changeregions():
  caminho = "Resources/KDA_Akali.jpg"
  imagem = cv.imread(caminho)

  if imagem is not None:
    (altura, largura) = imagem.shape[:2]
    (p1m, p2m) = (largura // 2, altura // 2)

    imagem_1 = imagem.copy()

    imagem_1[:p1m,:p2m] = imagem[p1m:,p1m:]
    imagem_top = imagem_1.copy()
    imagem_top[:p2m,p1m:] = imagem[p2m:,:p1m]

    imagem_tres_quadros = imagem_top.copy()
    imagem_tres_quadros[p2m:,:p1m] = imagem[:p2m,p1m:]
    imagem_complete = imagem_tres_quadros.copy()
    imagem_complete[p1m:,p2m:] = imagem[:p1m,:p1m]

    # cv.imshow("Trocar de Posicao a Imagem", imagem_1)
    # cv.imshow("Trocar de Posicao a Imagem", imagem_top)
    # cv.imshow("Trocar de Posicao a Imagem", imagem_tres_quadros)
    cv.imshow("Trocar de Posicao a Imagem", imagem_complete)
    cv.waitKey(0)
    cv.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

changeregions()