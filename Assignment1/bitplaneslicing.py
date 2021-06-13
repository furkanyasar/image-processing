import numpy as np
import cv2
from matplotlib import pyplot as plt
from myfunctions import scale8 #transform image to uint8

def bitplaneop(inimg, bitplaneNumber):
    bitplane=np.full_like(inimg,2**bitplaneNumber)
    return np.bitwise_and(inimg, bitplane)

def  bitplaneslicing(inimg, bitplaneNumber, allorone="no"):
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg, 0)
    else:
        input_image=inimg
    
    bitplanes=[]
    for bitplane in range(8):
        img=bitplaneop(input_image, bitplane)
        img=scale8(img)
        bitplanes.append(img)

    #bitplanes=bitplanes[::-1]

    if allorone==all:
        plt.subplot(331), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)) 
        plt.title('Original')
        plt.subplot(332), plt.imshow(cv2.cvtColor(bitplanes[0], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 1')
        plt.subplot(333), plt.imshow(cv2.cvtColor(bitplanes[1], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 2')
        plt.subplot(334), plt.imshow(cv2.cvtColor(bitplanes[2], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 3')
        plt.subplot(335), plt.imshow(cv2.cvtColor(bitplanes[3], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 4')
        plt.subplot(336), plt.imshow(cv2.cvtColor(bitplanes[4], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 5')
        plt.subplot(337), plt.imshow(cv2.cvtColor(bitplanes[5], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 6')
        plt.subplot(338), plt.imshow(cv2.cvtColor(bitplanes[6], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 7')
        plt.subplot(339), plt.imshow(cv2.cvtColor(bitplanes[7], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane 8')
        plt.show()
    else:
        plt.subplot(121), plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)) 
        plt.title('Original')
        plt.subplot(122), plt.imshow(cv2.cvtColor(bitplanes[bitplaneNumber], cv2.COLOR_BGR2RGB)) 
        plt.title('Bit Plane {0}'.format(bitplaneNumber))
        plt.show()
    return bitplanes[bitplaneNumber]

