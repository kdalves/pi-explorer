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


def tiltshift(frame):
    height = frame.shape[0]

    top_limit = top_bar_slider*height//100

    original_frame = frame.copy()

    if top_limit > 0:
        frame[:top_limit] = cv2.GaussianBlur(
            frame[:top_limit], (gauss_bar_slider, gauss_bar_slider), 0)

    bottom_limit = height - (bottom_bar_slider*height//100) - 1

    if bottom_limit == 255 + 1:
        bottom_limit = bottom_limit - 1

    if bottom_limit > 0:
        frame[bottom_limit:] = cv2.GaussianBlur(
            frame[bottom_limit:], (gauss_bar_slider, gauss_bar_slider), 0)

    x = np.arange(frame.shape[0], dtype=np.float32)

    alpha_x = (np.tanh((x - top_limit) / decay_bar_slider) -
               np.tanh((x - bottom_limit) / decay_bar_slider)) / 2

    mask = np.repeat(alpha_x, frame.shape[1]).reshape(frame.shape[:2])

    blur = cv2.GaussianBlur(
        frame, (gauss_bar_slider * 2 + 1, gauss_bar_slider * 2 + 1), 0)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    frame[:top_limit] = original_frame[:top_limit]
    frame[bottom_limit:] = original_frame[bottom_limit:]

    result = cv2.convertScaleAbs(frame * mask + blur * (1 - mask))

    return result


def on_top_bar_slide(value):
    global top_bar_slider

    top_bar_slider = value


def on_bottom_bar_slide(value):
    global bottom_bar_slider

    bottom_bar_slider = value


def on_gauss_bar_slider(value):
    global gauss_bar_slider

    if value % 2 == 0:
        value = value + 1

    if value == 0:
        value = 1

    gauss_bar_slider = value


def on_decay_bar_slider(value):
    global decay_bar_slider

    if value % 2 == 0:
        value = value + 1

    decay_bar_slider = value


def main():
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("main", 1)

    cv2.createTrackbar("Top x {0}".format(top_bar_slider_max), "main", top_bar_slider,
                       top_bar_slider_max, on_top_bar_slide)
    cv2.createTrackbar("Bottom x {0}".format(bottom_bar_slider_max), "main", bottom_bar_slider,
                       bottom_bar_slider_max, on_bottom_bar_slide)
    cv2.createTrackbar("Gauss x {0}".format(gauss_bar_slider_max), "main", gauss_bar_slider,
                       gauss_bar_slider_max, on_gauss_bar_slider)
    cv2.createTrackbar("Decay x {0}".format(decay_bar_slider_max), "main", decay_bar_slider,
                       decay_bar_slider_max, on_decay_bar_slider)

    speed = 4
    skip_frame = 0

    while True:
        ret, frame = cap.read()

        if skip_frame == 0:
            result = tiltshift(frame)
            cv2.imshow("main", result)

            skip_frame = (skip_frame + 1) % speed
        else:
            skip_frame = (skip_frame + 1) % speed

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey()


if __name__ == '__main__':
    main()