import numpy as np
import cv2
from matplotlib import pyplot as plt
from padImage import padImage
from cropImage import cropImage
from filterImage import filterImage
from unsharpMasking import unsharpMasking
from orderStFiltering import orderStFiltering


padImage('images\lena.png', 250,250)



cropImage('images\cameraman.jpg', [0,0,68,200])

filterImage('images\cameraman.jpg', 1)


orderStFiltering('images\lena.png',9,2)

unsharpMasking('images\cameraman.jpg',1,2)

