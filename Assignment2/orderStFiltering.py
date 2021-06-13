import numpy as np
import cv2 
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

def  orderStFiltering(inimg, filterSize,typeOfStatistics, showall="no"):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg)
    else:
        input_image=inimg
    
    if typeOfStatistics==1: #median
        median = cv2.medianBlur(input_image,filterSize)
        cv2.imshow('median', median)
    elif typeOfStatistics==2:#max
        img = Image.open(inimg)
        max = img.filter(ImageFilter.MaxFilter(size = filterSize))
        max.show('asd')
    elif typeOfStatistics==3: #min
        img = Image.open(inimg)
        min = img.filter(ImageFilter.MinFilter(size = filterSize))
        min.show()
     
    elif showall=="yes":
        im1 = Image.open(inimg)
        median = cv2.medianBlur(input_image,filterSize)
        max = im1.filter(ImageFilter.MaxFilter(size = filterSize))
        min = im1.filter(ImageFilter.MinFilter(size = filterSize))
        plt.subplot(221), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)) 
        plt.title('Original')
        plt.subplot(222), plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB)) 
        plt.title('median')
        plt.subplot(223), plt.imshow(max) 
        plt.title('max')
        plt.subplot(224), plt.imshow(min) 
        plt.title('min')
        plt.show()
    else:
        print('error')
    #cv2.imshow('outimg', median)
    #cv2.waitKey(0)
    
#orderStFiltering('images\lena.png',9,2)