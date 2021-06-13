import numpy as np
import cv2
from matplotlib import pyplot as plt
from myfunctions import scale8 #transform image to uint8


def histogramEqualization(inimg, bin):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg
    histogram, bins = np.histogram(input_image, bin, range=(0,bin))
    normalized=histogram/input_image.size
    cumul=np.cumsum(normalized)
    trans=cumul*(bin - 1)
    shape=input_image.shape
    ravel=input_image.ravel()
    equalizedHist=np.zeros_like(ravel)

    for i, px in enumerate(ravel):
        equalizedHist[i]=trans[px]

    outimg=equalizedHist.reshape(shape).astype(np.uint8)
   
    plt.subplot(121), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)) 
    plt.title('Original')
    plt.subplot(122), plt.imshow(cv2.cvtColor(outimg, cv2.COLOR_BGR2RGB)) 
    plt.title('Histogram Equalization')
    plt.show()
  
    return 
