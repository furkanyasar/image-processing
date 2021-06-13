import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp


def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def gaussianHP(img,D0):
    rows, cols = img.shape[:2]
    base = np.ones((rows,cols))
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def gaussianHPF(img,D0):
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    HighPassCenter = center * gaussianHP(img,D0)
    HighPass = np.fft.ifftshift(HighPassCenter)
    inverse_HighPass = np.fft.ifft2(HighPass)


     #Plotting
    plt.figure(figsize=(7, 7))
    plt.subplot(221),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(np.log(1+np.abs(center)), cmap ="gray"),plt.title("Mag Spectrum of Original Image")
    plt.subplot(223),plt.imshow(np.abs(inverse_HighPass), cmap = 'gray')
    plt.title('Gaussian HP')
    plt.subplot(224), plt.imshow(np.log(1+np.abs(HighPassCenter)), cmap ="gray"),plt.title("Mag Spectrum multiply HP Filter")
    plt.show()

    return inverse_HighPass

#img = cv2.imread('images\zelda.png',0)
#gaussianHPF(img,10)

