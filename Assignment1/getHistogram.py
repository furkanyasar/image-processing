import numpy as np
import cv2
from matplotlib import pyplot as plt
from myfunctions import scale8 #transform image to uint8


def getHistogram(inimg, bin):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg
    histogram, bins = np.histogram(input_image, bin, range=(0,bin))
    print(histogram)
    plt.hist(histogram,bins, edgecolor='black')
    plt.show()
    
    histogramValues = histogram
    return histogramValues