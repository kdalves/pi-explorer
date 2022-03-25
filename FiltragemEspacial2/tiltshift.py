import cv2
import numpy as np

gauss_bar_slider = 1
gauss_bar_slider_max = 100

decay_bar_slider = 1
decay_bar_slider_max = 100

top_bar_slider = 0
top_bar_slider_max = 100

bottom_bar_slider = 0
bottom_bar_slider_max = 100

original_image = cv2.imread("Resources/blend1.jpg")
image = original_image.copy()

if type(image).__module__ != "numpy":
    print("Arquivo não encontrado")


def tiltshift():
    global image
    global top_limit
    global bottom_limit

    top_limit = top_bar_slider*255//100
    image[top_limit:] = original_image[top_limit:]

    if top_limit > 0:
        image[:top_limit] = cv2.GaussianBlur(
            original_image[:top_limit], (gauss_bar_slider, gauss_bar_slider), 0)

    bottom_limit = 255 - (bottom_bar_slider*255//100) + 1

    if bottom_limit == 256:
        bottom_limit = bottom_limit - 1

    if bottom_limit > 0:
        image[bottom_limit:] = cv2.GaussianBlur(
            original_image[bottom_limit:], (gauss_bar_slider, gauss_bar_slider), 0)

    x = np.arange(image.shape[0], dtype=np.float32)

    alpha_x = (np.tanh((x - top_limit) / decay_bar_slider) -
               np.tanh((x - bottom_limit) / decay_bar_slider)) / 2

    mask = np.repeat(alpha_x, image.shape[1]).reshape(image.shape[:2])

    blur = cv2.GaussianBlur(
        image, (gauss_bar_slider * 2 + 1, gauss_bar_slider * 2 + 1), 0)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    image[:top_limit] = original_image[:top_limit]
    image[bottom_limit:] = original_image[bottom_limit:]

    result = cv2.convertScaleAbs(image * mask + blur * (1 - mask))

    cv2.imshow("main", result)


def on_top_bar_slide(value):
    global top_bar_slider

    top_bar_slider = value
    tiltshift()


def on_bottom_bar_slide(value):
    global bottom_bar_slider

    bottom_bar_slider = value
    tiltshift()


def on_gauss_bar_slider(value):
    global gauss_bar_slider

    if value % 2 == 0:
        value = value + 1

    if value == 0:
        value = 1

    gauss_bar_slider = value
    tiltshift()


def on_decay_bar_slider(value):
    global decay_bar_slider

    if value % 2 == 0:
        value = value + 1

    decay_bar_slider = value
    tiltshift()


def main():
    cv2.namedWindow("main", 1)

    cv2.createTrackbar("Top x {0}".format(top_bar_slider_max), "main", top_bar_slider,
                       top_bar_slider_max, on_top_bar_slide)
    cv2.createTrackbar("Bottom x {0}".format(bottom_bar_slider_max), "main", bottom_bar_slider,
                       bottom_bar_slider_max, on_bottom_bar_slide)
    cv2.createTrackbar("Gauss x {0}".format(gauss_bar_slider_max), "main", gauss_bar_slider,
                       gauss_bar_slider_max, on_gauss_bar_slider)
    cv2.createTrackbar("Decay x {0}".format(decay_bar_slider_max), "main", decay_bar_slider,
                       decay_bar_slider_max, on_decay_bar_slider)

    cv2.waitKey()


if __name__ == '__main__':
    main()