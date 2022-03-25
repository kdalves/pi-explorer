import cv2

TOP_SLIDER = 10
TOP_SLIDER_MAX = 200
top_bar_slider_inicial = 5
top_bar_slider = 10
edges = 0

caminho = 'Resources/deteccao_de_bordas/shoto-todoroki2.jpg'
imagem = cv2.imread(caminho, 0)


def on_trackbar_canny(value):
  global top_bar_slider
  top_bar_slider = value

  if top_bar_slider < TOP_SLIDER:
    top_bar_slider = 10

  edges = cv2.Canny(imagem, top_bar_slider, 3*top_bar_slider) 
  cv2.imshow("Deteccao de Bordas Cannys", edges)


def main():
  if imagem is not None:
    edges = cv2.Canny(imagem, top_bar_slider, 3*top_bar_slider) 
    cv2.imshow("Deteccao de Bordas Cannys", edges)
    cv2.createTrackbar("Bordas", "Deteccao de Bordas Cannys", top_bar_slider_inicial, TOP_SLIDER_MAX, on_trackbar_canny)

    cv2.waitKey(0)     
    cv2.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

if __name__ == '__main__':
    main()
