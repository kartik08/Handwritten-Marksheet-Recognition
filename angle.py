import cv2
import numpy as np
import math
from scipy.ndimage import rotate
from binary import binarization1
from crop import crop
def ccl(img):
    #connected componets labeliing
    ret, labels = cv2.connectedComponents(img,8,cv2.CV_32S)
    #calculate the no of connected labelling
    unique, counts = np.unique(labels, return_counts=True)
    counts=np.reshape(counts,(1,np.size(counts)))
    counts[0,0]=0
    #finding the maximum connectivity
    n = int(np.where(counts == np.amax(counts))[1])
    [r,c]=img.shape
    i_label=np.where(labels!=n,0,labels)
    temp=0
    for i in range(r):
        for j in range(c):
            if i_label[i][j]==n:
                temp=1
                break;
        if temp==1:
            break;
    x1=i
    y1=j
    temp=0
    for j in range(c-1,-1,-1):
        for i in range(r):
             if i_label[i][j]==n and i_label[i+1][j]==n:
                temp=1
                break;
        if temp==1:
            break;
    x=i-x1
    y=j-y1
    #finding the angle
    theta=(math.degrees(math.atan(x/y)))
    #rotating the image
    img1=(binarization1((rotate(img, theta))))
    return (img1)
def anglec(img1):
    [r,c]=img1.shape
    temp=0
    for i in range(200):
        for j in range(100):
            if img1[i][j]==1:
                x1=i
                y1=j
                temp=1
                break;
        if temp==1:
            break;
    temp=0
    for i in range(200):
        for j in range(c-1,c-100,-1):
            if img1[i][j]==1:
                x2=i-x1
                y2=j-y1
                temp=1
                break;
        if temp==1:
            break;
    theta=(math.degrees(math.atan(x2/y2)))
    img1=(binarization1((rotate(img1, theta))))
    img1=crop(img1)
    return(img1)
