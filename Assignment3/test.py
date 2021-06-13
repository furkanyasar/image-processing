import numpy as np
import cv2
from matplotlib import pyplot as plt
from sinc import sinc
from stripe import stripe
from circle import circle
from rect import rectangle

def dft(img):
    f=np.fft.fft2(img)
    shift=np.fft.fftshift(f)
    mag_spec=20*np.log(np.abs(shift))
    mag_spec=np.asarray(mag_spec, dtype=np.uint8)
    cv2.imshow('DFT of Image',mag_spec)
    cv2.waitKey(0)
    return mag_spec

a=stripe(50,"v") #if type any other char for second argument, function returns horizontal 
b=circle(50)
c=rectangle(100,60)
d=sinc(60)

dft_list=(a,b,c,d)
dft_out=[]
for i in dft_list: 
    x=dft(i) 
    dft_out.append(x)

plt.figure(figsize=(10, 7))
plt.subplot(241), plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB)) 
plt.title('Stripe')
plt.subplot(242), plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB)) 
plt.title('Circle')
plt.subplot(243), plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB)) 
plt.title('Rectangle')
plt.subplot(244), plt.imshow(cv2.cvtColor(d, cv2.COLOR_BGR2RGB)) 
plt.title('Sinc')
plt.subplot(245), plt.imshow(cv2.cvtColor(dft_out[0], cv2.COLOR_BGR2RGB)) 
plt.title('DFT of Stripe')
plt.subplot(246), plt.imshow(cv2.cvtColor(dft_out[1], cv2.COLOR_BGR2RGB)) 
plt.title('DFT of Circle')
plt.subplot(247), plt.imshow(cv2.cvtColor(dft_out[2], cv2.COLOR_BGR2RGB)) 
plt.title('DFT of Rectangle')
plt.subplot(248), plt.imshow(cv2.cvtColor(dft_out[3], cv2.COLOR_BGR2RGB)) 
plt.title('DFT of Sinc')
plt.show()




