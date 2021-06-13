import numpy as np
import cv2
from matplotlib import pyplot as plt
from myfunctions import scale8 #transform image to uint8


def  graylevelslicing(inimg, beginingPoint, finishPoint):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg

    h,w =input_image.shape[:2]
    outimg=np.zeros((h,w))
    for i in range(1, h):
        for j in range(1, w):
            if input_image[i,j]>=beginingPoint and input_image[i,j]<=finishPoint:
                outimg[i,j]=255
            else:
                outimg[i,j]=0
    
    cv2.imshow('Gray Level Slicing',outimg)
    cv2.waitKey(0)
    
    return outimg


