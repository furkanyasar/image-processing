import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
from ideal import idealHPF
from butterworth import butterworthHPF
from gaussian import gaussianHPF
from laplacian import laplacian




img = cv2.imread('images\drone.tif',0)

#img = cv2.imread("images\print-pattern.tif", 0)

img = cv2.resize(img,(256,256))

idealHPF(img,14)

butterworthHPF(img,14,2)

gaussianHPF(img,14)

laplacian(img)

