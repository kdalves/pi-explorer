import cv2
import numpy as np

image1 = cv2.imread("Resources/blend1.jpg")
image2 = cv2.imread("Resources/blend2.jpg")
imageTop = image2.copy()

if type(image1).__module__ != "numpy":
    print("Arquivo não encontrado")

if type(image2).__module__ != "numpy":
    print("Arquivo não encontrado")

alfa = 0.0
alfa_slider = 0
alfa_slider_max = 100
top_slider = 0
top_slider_max = 100
TrackbarName = ''


def on_trackbar_blend(param):
    global alfa_slider
    global alfa

    alfa_slider = param
    alfa = alfa_slider/alfa_slider_max
    blended = cv2.addWeighted(image1, 1-alfa, imageTop, alfa, 0.0)
    cv2.imshow("addweighted", blended)


def on_trackbar_line(top_slider):
    global imageTop

    imageTop = image1.copy()
    limit = top_slider*255//100
    if limit > 0:
        imageTop[:limit] = image2[:limit]
        cv2.imshow("addweighted", imageTop)

    on_trackbar_blend(alfa_slider)


def main():
    cv2.namedWindow("addweighted", 1)

    TrackbarName = "Alpha x {0}".format(alfa_slider_max)
    cv2.createTrackbar(TrackbarName, "addweighted", alfa_slider,
                       alfa_slider_max, lambda x: on_trackbar_blend(x))
    on_trackbar_blend(alfa_slider)

    TrackbarName = "Scanline x {0}".format(top_slider_max)
    cv2.createTrackbar(TrackbarName, "addweighted", top_slider,
                       top_slider_max, lambda x: on_trackbar_line(x))
    on_trackbar_line(top_slider)

    cv2.waitKey()


if __name__ == '__main__':
    main()