import numpy as np
import cv2
from matplotlib import pyplot as plt
import math



def dft(img):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    return dft_shift, magnitude_spectrum

def idft(img):
   
    f_ishift = np.fft.ifftshift(img)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
    return img_back

def laplacian(img):
  
    dim=256
    mask = np.zeros((dim,dim,2),np.uint8)
    for i in range(dim):
        for j in range(dim):
            dist=(i-dim/2)**2+(j-dim/2)**2
            mask[i, j] = 4*np.pi*dist
    #print('type:', type(4*np.pi*5), 4*np.pi*5)
    dft_shift, magnitude_spectrum = dft(img)
    laplace = dft_shift*np.absolute(mask)
    outimg=idft(laplace)
    
       #Plotting
    plt.figure(figsize=(7, 7))
    plt.subplot(131),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Mag. Spect. of Input'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(outimg, cmap = 'gray')
    plt.title('Laplacian HP'), plt.xticks([]), plt.yticks([])
    plt.show()
    return outimg, mask

#img = cv2.imread('images\LENA.png',0)
#img = cv2.resize(img,(256,256))
#outimg, mask=laplacian(img)