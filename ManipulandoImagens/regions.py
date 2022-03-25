import cv2 as cv

def reduzir_imagem(imagem):
  porcetagem_escala = 10
  comprimento = int(imagem.shape[1] * porcetagem_escala / 100)
  altura = int(imagem.shape[0] * porcetagem_escala / 100)
  dimensao_imagem = (comprimento, altura)
  return cv.resize(imagem, dimensao_imagem, interpolation = cv.INTER_AREA)

def regions(p1_c, p1_a, p2_c, p2_a):
  caminho = "Resources/Haru.jpg"
  imagem = cv.imread(caminho, cv.IMREAD_GRAYSCALE)

  if imagem is not None:    
    imagem_reduzida = reduzir_imagem(imagem)
    cv.namedWindow("Janela", cv.WINDOW_AUTOSIZE)

    imagem_reduzida[p1_c:p1_a,p2_c:p2_a] = 255 - imagem_reduzida[p1_c:p1_a,p2_c:p2_a]

    cv.imshow("Janela", imagem_reduzida)
    cv.waitKey(0)
    cv.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

regions(40,301,150,250)
# regions(60,350,50,200)
# regions(105,200,80,130)