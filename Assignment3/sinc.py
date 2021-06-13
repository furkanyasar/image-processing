import numpy as np
import cv2 
from matplotlib import pyplot as plt

def  sinc(f):
    

    x=np.arange(-128,128)
    y=np.sinc(2*np.pi*x/f)
    y += max(y)
    sinc = np.array([[y[j]*127 for j in range(256)] for i in range(256)], dtype=np.uint8)
    img=np.roll(sinc, 127, axis=1) # right
    
    cv2.imshow('sinc', sinc)
    
    cv2.waitKey(0)

    return sinc



#sinc(100)


