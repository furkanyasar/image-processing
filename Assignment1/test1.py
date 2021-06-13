import numpy as np
import cv2
from matplotlib import pyplot as plt
from bitplaneslicing import bitplaneslicing
from powerlawtransform import powerlawtransform
from graylevelslicing import graylevelslicing
from sampleImage import sampleImage
from quantizeImage import quantizeImage

#all functions take inimg input as a read image file or path
#inimg=cv2.imread('images\cameraman.jpg'0) #flag need to be = 0 for grayscale
#sampleImage(inimg, 16)

sampleImage('images\Barbara.bmp', 16)


quantizeImage('images\lena.png', 256)


graylevelslicing('images\cameraman.jpg', 32, 90)

powerlawtransform('images\zelda.png', 5)

#if you want to see all bit planes inpput the 3rd argument "all", 
#otherwise you can pass it
bitplaneslicing('images\cameraman.jpg', 5, all)
bitplaneslicing('images\cameraman.jpg', 7)
