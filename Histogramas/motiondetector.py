import cv2
import numpy as np


def main():
  nbins = 128
  histRange = [0, 255]

  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    print("Could not open video device")
    return

  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

  print(f"largura = {width}")
  print(f"altura = {height}")

  histw = nbins
  histh = nbins // 2

  old_frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)

  max_difference = 1000
  old_result = None

  first_iteration = True

  while(True):
    current_frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)

    current_frameHist = cv2.calcHist(current_frame, [0], None, [nbins], histRange)
    old_frameHist = cv2.calcHist(old_frame, [0], None, [nbins], histRange)

    result = cv2.compareHist(current_frameHist, old_frameHist, cv2.HISTCMP_KL_DIV)

    if not old_result:
      old_result = result

    difference = abs(result - old_result)

    if difference > max_difference:
      print(f"movement detected: {result} - difference: {difference} - max_difference: {max_difference}")
      print(f"ALERTA: MOVIMENTO DETECTADO!")

    cv2.imshow('frame', current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

    old_frame = current_frame
    old_result = result


  cv2.waitKey()


if __name__ == '__main__':
  main()