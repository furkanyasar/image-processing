import numpy as np
import cv2 
from matplotlib import pyplot as plt

def  stripe(f,direction="v"):
    

    x=np.arange(256)
    y=np.sin(2*np.pi*x/f)
    y += max(y)
    vertical = np.array([[y[j]*127 for j in range(256)] for i in range(256)], dtype=np.uint8)
    horizontal = vertical.T
    cv2.imshow('Vertical Stripes', vertical)
    cv2.imshow('Horizontal Stripes', horizontal)
    cv2.waitKey(0)
    if direction=="v":
        return vertical
    else:
        return horizontal
   


#stripe(50,"h")


