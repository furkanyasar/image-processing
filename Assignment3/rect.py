import numpy as np
import cv2 
from matplotlib import pyplot as plt


def  rectangle(x,y):


    img = np.zeros((256,256), np.uint8)
    img.fill(255)

    color = (0,0,0)
    thickness = 2

    topleft=(int(127-(x/2)),int(127-(y/2)))

    botright=(int(127+(x/2)),int(127+(y/2)))

    image = cv2.rectangle(img, topleft,botright,color, thickness)
    cv2.imshow('Rectangle', image)
    cv2.waitKey(0)

    return image


#rectangle(100,20)


