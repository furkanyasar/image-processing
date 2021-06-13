import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
from myfunctions import scale8 #transform image to uint8


def quantizeImage(inimg, q):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg
    h,w = input_image.shape[:2]
    L=int(q/5)
    buffer=np.zeros((q,1))
    for i in range(0,q):
        buffer[i,0] = math.floor(i/L)*L+L/2

    outimg=np.zeros(input_image.shape)


    for i in range(1,h+1):
        for j in range(1,w+1):
            outimg[i-1,j-1]=buffer[input_image[i-1,j-1]]
    
    outimg=scale8(outimg)

    print(buffer)
    plt.subplot(121),plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(outimg, cv2.COLOR_BGR2RGB))
    plt.title('Quantized Image - Ratio: {0}'.format(q))
    plt.show()
    return outimg
