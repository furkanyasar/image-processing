import numpy as np
import cv2 
from matplotlib import pyplot as plt


def  circle(radius):
    if radius>126:
        print('Error! Please input radius below 127')
        return -1


    img = np.zeros((256,256), np.uint8)
    img.fill(255)
    center_coordinates = (127, 127)
    #radius = 30
    color = (0,0, 0)
    thickness = 2
    circle = cv2.circle(img, center_coordinates, radius, color, thickness)
    cv2.imshow('Circle', circle)
    cv2.waitKey(0)
    return circle

#circle(61)


