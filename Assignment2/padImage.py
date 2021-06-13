import numpy as np
import cv2 
from matplotlib import pyplot as plt



def  padImage(inimg, nrp, ncp, display="yes"):
    """This function adds black border to input image and if desired shows result with imshow(). 
    Process steps:
    1.Creates black image with inimg size.
    2.Resize inimg to nrp x ncp.
    3.Centers te resized image into black image. 
    Arguments: 
        inimg {[image array] or [string]} -- {it can be image array, or path string for image}
        nrp {[int]} -- {Desired height, inimg resized to this height }
        ncp {[int]} -- {Desired weight, inimg resized to this weight}
    Kwargs:
        display{[string]} -- {[yes] for default, otherwise function will not show output image.}
    Returns:

        outimg {[image array]} -- {padded image returns}                            
    """
    if isinstance(inimg, str):
        input_image=cv2.imread(inimg)
    else:
        input_image=inimg

    h,w,c = input_image.shape
    pad=np.zeros((h,w,c),np.uint8)
    imgResize = cv2.resize(input_image,(ncp,nrp))

    yoff = round((h-nrp)/2)
    xoff = round((w-ncp)/2)
    outimg = pad.copy()
    outimg[yoff:yoff+nrp, xoff:xoff+ncp] = imgResize
    print('orig: ',input_image.shape)
    print('resized: ',imgResize.shape )
    if display=="yes":
        #cv2.imwrite('pad.jpg',outimg)
        #cv2.imshow('original {0}x{1}'.format(h,w), input_image)
        cv2.imshow('padded {0}x{1}'.format(nrp,ncp), outimg)
        cv2.waitKey(0)
    else:
        pass
    return outimg
    


#padImage('images\lena.png', 250,20,"no")
#padImage('images\lena.png', 250,250)