import numpy as np
import cv2
from matplotlib import pyplot as plt
from myfunctions import scale8 #transform image to uint8


def sampleImage(inimg, samplingRatio):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg
    h,w = input_image.shape[:2]
    x_new= round(h/samplingRatio)
    y_new= round(w/samplingRatio)

    x_scale = round(h/x_new)
    y_scale = round(w/y_new)

    buffer=np.zeros((x_new,y_new))


    for count1 in range(1,x_new+1):
        for count2 in range(1, y_new+1):
            buffer[count1-1,count2-1]=input_image[count1 * x_scale-1, count2 * y_scale-1]
    outimg=scale8(buffer)

    print(buffer)
    plt.subplot(121),plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(outimg, cv2.COLOR_BGR2RGB))
    plt.title('Sampled Image - Ratio: {0}'.format(samplingRatio))
    plt.show()
    return outimg

