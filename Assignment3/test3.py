import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def butterworthLP(D0,n):
    rows, cols = img.shape[:2]
    base = np.zeros((rows,cols))
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

img = cv2.imread("images\print-pattern.tif", 0)
original = np.fft.fft2(img)
center = np.fft.fftshift(original)

LowPassCenter = center * butterworthLP(50,10)
LowPass = np.fft.ifftshift(LowPassCenter)
inverse_LowPass = np.fft.ifft2(LowPass)

plt.figure(figsize=(5, 6.5))
plt.subplot(311), plt.imshow(np.abs(img), "gray"), plt.title("Original Image")
plt.subplot(312), plt.imshow(np.log(1+np.abs(LowPassCenter)), "gray"), plt.title("Centered Spectrum multiply LP Filter")
plt.subplot(313), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass")
plt.show()
