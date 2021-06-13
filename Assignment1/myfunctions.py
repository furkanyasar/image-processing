import numpy as np
import cv2

#transform image to uint8

def scale8(img):
    i=img.astype(float)
    i -= np.min(i)
    i /= np.max(i)
    return (i*255).astype(np.uint8)