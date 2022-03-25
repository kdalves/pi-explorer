import cv2
import numpy as np

def main():
  media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111]
  gauss = [0.0625, 0.125,  0.0625, 0.125, 0.25, 0.125,  0.0625, 0.125,  0.0625]
  horizontal = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
  vertical = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
  laplacian = [0, -1, 0, -1, 4, -1, 0, -1, 0]
  boost = [0, -1, 0, -1, 5.2, -1, 0, -1, 0]
  frameFiltered = np.zeros((3, 3))
  result = np.zeros((3, 3))

  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    print("Could not open video device")
    return

  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  mask = np.reshape(media, (3, 3))

  absolute = True

  while(True):
    ret, frame = cap.read()

    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("original", framegray)

    framegray = cv2.flip(framegray, 1)

    frame32f = np.float32(framegray)
    frameFiltered = cv2.filter2D(frame32f, cv2.CV_32F, mask, anchor=(1, 1), delta=0)

    if absolute:
      frameFiltered = np.abs(frameFiltered)

    result = np.uint8(frameFiltered)
    
    cv2.imshow("filtroespacial", result)

    key = cv2.waitKey(10)

    if key != -1:
      key = chr(key)

    if key == '\x1b':
      break

    if key == 'a':
      absolute = not absolute
    elif key == 'm':
      mask = np.reshape(media, (3, 3))
      print(mask)
    elif key == 'g':
      mask = np.reshape(gauss, (3, 3))
      print(mask)
    elif key == 'h':
      mask = np.reshape(horizontal, (3, 3))
      print(mask)
    elif key == 'v':
      mask = np.reshape(vertical, (3, 3))
      print(mask)
    elif key == 'l':
      mask = np.reshape(laplacian, (3, 3))
      print(mask)
    elif key == 'b':
      mask = np.reshape(boost, (3, 3))
      print(mask)
    elif key == 't':
      mask = np.float32(np.concatenate((np.reshape(gauss, (3, 3)), np.reshape(laplacian, (3, 3)))))
      print(mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break 

  cv2.waitKey()


if __name__ == '__main__':
  main()
