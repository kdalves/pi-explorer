import cv2
import numpy as np


def main():
  nbins = 128
  histRange = [0, 255]

  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    print("camera indisponiveis")
    return

  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

  print(f"largura = {width}")
  print(f"altura = {height}")

  histw = nbins
  histh = nbins // 2

  histImgR = np.zeros((histh, histw, 3), dtype="uint8")
  histImgG = np.zeros((histh, histw, 3), dtype="uint8")
  histImgB = np.zeros((histh, histw, 3), dtype="uint8")

  while(True):
    ret, frame = cap.read()

    planes = cv2.split(frame)

    histR = cv2.calcHist(planes[0], [1], None, [nbins], histRange)
    histG = cv2.calcHist(planes[1], [1], None, [nbins], histRange)
    histB = cv2.calcHist(planes[2], [1], None, [nbins], histRange)

    cv2.normalize(histR, histR, 0, histImgR.shape[1], cv2.NORM_MINMAX, -1)
    cv2.normalize(histG, histG, 0, histImgG.shape[1], cv2.NORM_MINMAX, -1)
    cv2.normalize(histB, histB, 0, histImgB.shape[1], cv2.NORM_MINMAX, -1)

    histImgR = np.zeros((histh, histw, 3), dtype="uint8")
    histImgG = np.zeros((histh, histw, 3), dtype="uint8")
    histImgB = np.zeros((histh, histw, 3), dtype="uint8")

    for i in range(nbins):
      cv2.line(histImgR, (i, histh),
               (i, histh - round(histR[i][0])), [0, 0, 255], 1, 8, 0)
      cv2.line(histImgG, (i, histh),
               (i,  histh - round(histG[i][0])), [0, 255, 0], 1, 8, 0)
      cv2.line(histImgB, (i, histh),
               (i,  histh - round(histB[i][0])), [255, 0, 0], 1, 8, 0)

    imgR = histImgR.copy()
    imgG = histImgG.copy()
    imgB = histImgB.copy()

    cv2.rectangle(imgR, (0, 0), (nbins, histh),  [0, 0, 255])
    cv2.rectangle(imgG, (0, histh), (nbins, histh),  [0, 255, 0])
    cv2.rectangle(imgB, (0, 2*histh), (nbins, histh),  [255, 0, 0])

    cv2.imshow('Hist. Verm.', imgR)
    cv2.imshow('Hist. Verde', imgG)
    cv2.imshow('Hist. Azul', imgB)
    cv2.imshow('Imagem', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cv2.waitKey()


if __name__ == '__main__':
  main()
