#filter son

import numpy as np
import cv2 
from matplotlib import pyplot as plt
from padImage import padImage

def  filterImage(inimg, filter, manual="no"):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg)
    else:
        input_image=inimg
    h,w = input_image.shape[:2]
    #padding with zeros
    img=input_image.copy()
    input_image=padImage(input_image,h-1,w-1,display="no")

    xdir=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    ydir=np.array([-1,-1,-1,0,0,0,1,1,1]).reshape(3,3)
    laplace=np.array([0,1,0,1,-4,1,0,1,0]).reshape(3,3)
    gaus=np.array([0.0233,0.106,0.0233,0.106,0.421,0.106,0.0233,0.106,0.0233]).reshape(3,3)
    uniavg=np.array([1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9]).reshape(3,3)

    kernel=[xdir,ydir,laplace,gaus,uniavg]
    results=[]
    for kernel in kernel:
        outimg=cv2.filter2D(input_image, -1, kernel)
        cv2.imshow('out',outimg)
        results.append(outimg)
        #cv2.imwrite('out.jpg',outimg)
        cv2.waitKey(0)

    if manual=="yes":
        outimg=cv2.filter2D(input_image, -1, filter)
        cv2.imshow('out',outimg)
        cv2.waitKey(0)
        
    """
    plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
    plt.title('Original')
    plt.subplot(232), plt.imshow(cv2.cvtColor(kernel[0], cv2.COLOR_BGR2RGB)) 
    plt.title('x directional high pass filter')
    plt.subplot(233), plt.imshow(cv2.cvtColor(kernel[1], cv2.COLOR_BGR2RGB)) 
    plt.title('y directional high pass filter')
    plt.subplot(234), plt.imshow(cv2.cvtColor(kernel[2], cv2.COLOR_BGR2RGB)) 
    plt.title('Laplacian filter')
    plt.subplot(235), plt.imshow(cv2.cvtColor(kernel[3], cv2.COLOR_BGR2RGB)) 
    plt.title('Gaussian averaging filter')
    plt.subplot(236), plt.imshow(cv2.cvtColor(kernel[4], cv2.COLOR_BGR2RGB)) 
    plt.title('Uniform averaging filter')
    plt.show()
    """

#filterImage('images\cameraman.jpg', 1)
