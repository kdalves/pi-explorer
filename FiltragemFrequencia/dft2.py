import cv2
import numpy as np
import math

gamma_low_slider = 0
gamma_low_slider_max = 100

gamma_high_slider = 0
gamma_high_slider_max = 100

d0_slider = 50
d0_slider_max = 100

c_slider = 5
c_slider_max = 100

dft_M = None
dft_N = None


image = cv2.imread("Resources/blend1.jpg")

if type(image).__module__ != "numpy":
    print("Arquivo nao encontrado")


image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def homomorphic():
    gl = gamma_low_slider // 100
    gh = gamma_high_slider // 100
    d0 = 25 * d0_slider // 100
    c = c_slider // 100

    cv2.imshow("original", image_gray)

    padded = cv2.copyMakeBorder(image_gray, 0,  dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT)

    zeros = np.float32(np.zeros(padded.shape))

    real_input = np.float32(padded.copy())

    planos = [real_input, zeros]

    complex_image = cv2.merge(planos)

    tmp = np.float32(np.zeros((dft_M, dft_N)))

    complex_image = cv2.dft(complex_image)

    complex_image = move_dft(complex_image)

    for x in range(tmp.shape[0]):
        for y in range(tmp.shape[1]):
            d2 = (x-dft_M//2)*(x-dft_M//2)+(y-dft_N//2)*(y-dft_N//2)

            tmp[x, y] = (gamma_high_slider-gamma_low_slider) * \
                (1 - math.exp(-(c*d2/(d0*d0)))) + gamma_low_slider

    comps = [tmp, tmp]
    my_filter = cv2.merge(comps)
    complex_image = np.float32(complex_image)
    complex_image = cv2.mulSpectrums(complex_image, my_filter, 0)

    complex_image = move_dft(complex_image)

    complex_image = cv2.idft(complex_image)

    planos = cv2.split(complex_image)

    cv2.normalize(planos[0], planos[0], 0, 1, cv2.NORM_MINMAX)
    cv2.imshow("filtrada", planos[0])


def move_dft(image):
    cx = image.shape[0] // 2
    cy = image.shape[1] // 2

    A = image[:cx, :cy]
    B = image[:cx, cy:]
    C = image[cx:, :cy]
    D = image[cx:, cy:]

    tmp = A.copy()
    A = D.copy()
    D = tmp.copy()

    tmp = C.copy()
    C = B.copy()
    B = tmp.copy()

    image[:cx, :cy] = A
    image[:cx, cy:] = B
    image[cx:, :cy] = C
    image[cx:, cy:] = D

    return image


def on_gamma_low_slider(value):
    global gamma_low_slider

    gamma_low_slider = value
    homomorphic()


def on_gamma_high_slider(value):
    global gamma_high_slider

    gamma_high_slider = value
    homomorphic()


def on_d0_slider(value):
    global d0_slider

    d0_slider = value
    homomorphic()


def on_c_slider(value):
    global c_slider

    c_slider = value
    homomorphic()


def main():
    global dft_M
    global dft_N

    cv2.namedWindow("original", 1)
    cv2.namedWindow("homomorphic", 1)

    dft_M = cv2.getOptimalDFTSize(image.shape[0])
    dft_N = cv2.getOptimalDFTSize(image.shape[1])

    cv2.createTrackbar("Gamma Low", "homomorphic", gamma_low_slider,
                       gamma_low_slider_max, on_gamma_low_slider)
    cv2.createTrackbar("Gamma High", "homomorphic", gamma_high_slider,
                       gamma_high_slider_max, on_gamma_high_slider)
    cv2.createTrackbar("d_zero", "homomorphic", d0_slider,
                       d0_slider_max, on_d0_slider)
    cv2.createTrackbar("c", "homomorphic", c_slider,
                       c_slider_max, on_c_slider)

    homomorphic()

    cv2.waitKey()


if __name__ == '__main__':
    main()