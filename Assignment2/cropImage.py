import numpy as np
import cv2 
from matplotlib import pyplot as plt



def  cropImage(inimg, cropArray):
    
    """
    This function crops the input image and shows it with imshow().

    Arguments: 
        inimg {[image array] or [string]} -- {it can be image array, or path string for image}
        croppArray {[list]} -- {It is an array, takes crop coordinates}
                               {[top,left,bottom,right]}
    Returns:

        outimg {[image array]} -- {cropped image returns}                               

    """

    if isinstance(inimg, str):
        input_image=cv2.imread(inimg)
    else:
        input_image=inimg
    print('Original Image Size:',input_image.shape)

    top = cropArray[0]
    left = cropArray[1]
    bottom = cropArray[2]
    right = cropArray[3]
    
    outimg = input_image[top:bottom, left:right]
   
    print('Cropped Image Size:',outimg.shape)
    #cv2.imwrite('crop.jpg',outimg)
    cv2.imshow('Cropped', outimg)
    cv2.waitKey(0)
    return outimg


#cropImage('images\cameraman.jpg', [0,0,68,200])
