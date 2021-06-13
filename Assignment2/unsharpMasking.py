import numpy as np
import cv2 
from matplotlib import pyplot as plt
from skimage import io
from skimage.filters import unsharp_mask


def  unsharpMasking(inimg, lowPassFilter,k):
    img=io.imread(inimg)
    
    ushrp=unsharp_mask(img,radius=3, amount=k)
    #laplace=np.array([0,-1,0,-1,4,-1,0,-1,0]).reshape(3,3)
    #filter=lowPassFilter.reshape(3,3)
    #filterImage
    plt.subplot(121), plt.imshow(img) 
    plt.title('Original')
    plt.subplot(122), plt.imshow(ushrp) 
    plt.title('Unsharp Masked')
    plt.show()

#unsharpMasking('images\cameraman.jpg',1,2)


