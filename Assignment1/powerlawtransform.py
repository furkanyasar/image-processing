import numpy as np
import cv2
from matplotlib import pyplot as plt


def powerlawtransform(inimg, power):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg
    double=cv2.normalize(input_image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
    powerlaw= 2*(double**power)
    outimg = powerlaw * (255.0)
    outimg = outimg.astype(np.uint8)
    plt.subplot(221), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(222), plt.imshow(cv2.cvtColor(outimg, cv2.COLOR_BGR2RGB))
    plt.title('Power Law Transform Applied')
    plt.show()

    return outimg

