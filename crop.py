import cv2
import numpy as np
def crop(img1):
    ret, labels = cv2.connectedComponents(img1,8,cv2.CV_32S)
    unique, counts = np.unique(labels, return_counts=True)
    counts=np.reshape(counts,(1,np.size(counts)))
    counts[0,0]=0
    n = int(np.where(counts == np.amax(counts))[1])
    [r,c]=img1.shape
    i_label=np.where(labels!=n,0,labels)
    temp=0
    for i in range(r):
        for j in range(c):
            if i_label[i][j]==n:
                x=i;
                temp=1
                break;
        if temp==1:
            temp=0;
            break;
    for i in range(r-1,-1,-1):
        for j in range(c):
            if i_label[i][j]==n:
                x1=i;
                temp=1
                break;
        if temp==1:
            temp=0;
            break;
    for j in range(c):
        for i in range(r):
            if i_label[i][j]==n:
                y=list(range(0,j-1));
                temp=1
                break;
        if temp==1:
            temp=0;
            break;
    for j in range(c-1,-1,-1):
        for i in range(r):
            if i_label[i][j]==n:
                y1=list(range(j+1,c));
                temp=1
                break;
        if temp==1:
            temp=0;
            break;
    img1=img1[x-1:x1+1]
    img1=np.delete(img1,y1,1)
    img1=np.delete(img1,y,1)
    return(img1)
