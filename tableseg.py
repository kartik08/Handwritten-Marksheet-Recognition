import numpy as np
import cv2

def format(img):
    
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
    img1=np.zeros((r,c))
    rows=np.sum(i_label, axis=1)
    coloumn=np.sum(i_label, axis=0)
    temp=0
    for i in range(r):
        if rows[i]>.90*c and i>8 and i<r-8:
            img1[i,:]=1#i_label[i,:]
            if i>50:
                if temp==0:
                    temp=i;
        elif i<8 or i>r-8:
            img1[i,:]=1
    for i in range(c):
        if coloumn[i]>.8*r and i>8 and i<c-8:
            img1[:,i]=1#i_label[:,i]
        elif i<8 or i>c-8:
            img1[:,i]=1
    img2=i_label[0:temp,:];
    imghi=img[0:temp,:];
    imgmt=img1[temp:,:]
    imgmi=img[temp:,:]
    [r,c]=img2.shape
    img3=np.zeros((r,c))
    img4=np.zeros((r,c))
    rows=np.sum(img2, axis=1)
    coloumn=np.sum(img2, axis=0)
    for i in range(r):
        if i <8:
            img3[i,:]=1
        elif rows[i]>.4*c:
            img3[i,:]=img2[i,:]
    for j in range(c):
        if j<8 or j>c-8:
            img4[:,j]=1
        elif coloumn[j]>.5*r:
            img4[:,j]=img2[:,j]
    return(img4,imghi,imgmt,imgmi,)
