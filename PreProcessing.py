import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from crop import crop
from angle import anglec,ccl
from binary import binarization
from tableseg import format
from contrast import contrast
from corner import corner
start=time.time()
#Reading the image
img1=(cv2.imread("D:\Project\marksheets\\1.jpg",1))
#Increasing contrast
img1=contrast(img1)
#binarization of the image using the otsu algorithem
img1=binarization(img1)
## Perform the operation of tilt and croping
img1=crop(img1)
img1=ccl(img1)
img1=crop(img1)
img1=anglec(img1)
imght,imghi,imgmt,imgmi=format(img1)
corner(imgmt,imgmi)
#Displaying the image
##plt.imshow(imgmt,cmap="gray")
end=time.time()
##plt.show()
print(end-start)
    
