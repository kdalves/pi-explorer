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

  while(True):

    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    equalizedFrame = cv2.equalizeHist(frame)

    equalizedHist = cv2.calcHist(equalizedFrame, [0], None, [nbins], histRange)
    frameHist = cv2.calcHist(frame, [0], None, [nbins], histRange)

    histImg = np.zeros((histh, histw), dtype="uint8")
    histFrame = np.zeros((histh, histw), dtype="uint8")

    cv2.normalize(equalizedHist, equalizedHist, 0,
                  histImg.shape[1], cv2.NORM_MINMAX, -1)
    cv2.normalize(frameHist, frameHist, 0,
                  histFrame.shape[1], cv2.NORM_MINMAX, -1)

    for i in range(nbins):
      cv2.line(histImg, (i, histh),
               (i, histh - round(equalizedHist[i][0])), [255], 1, 8, 0)
      cv2.line(histFrame, (i, histh),
               (i, histh - round(frameHist[i][0])), [255], 1, 8, 0)

    img = histImg.copy()
    imgFrame = histFrame.copy()

    cv2.rectangle(img, (0, 0), (nbins, histh), [0])
    cv2.rectangle(imgFrame, (0, 0), (nbins, histh), [0])

    cv2.imshow('equalizedHist', img)
    cv2.imshow('equalized', equalizedFrame)

    cv2.imshow('frameHist', imgFrame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cv2.waitKey()


if __name__ == '__main__':
  main()
