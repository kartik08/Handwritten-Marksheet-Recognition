import numpy as np
import matplotlib.pyplot as plt
import cv2
def charseg(img):
    [r,c]=img.shape
    n=np.sum(img,axis=0)
    i=0;
    plt.imshow(img,cmap="gray")
    plt.show()
    char=np.zeros((r,c))
    while(i<c):
        if n[i]>5 and i!=c-1:
            temp=i
            k=0;
            for j in range(i,c,1):
                if n[j]<5 and k>5:
                    if j==c-1:
                        i=c;
                        break;
                    char=img[:,temp:j-1];
                    char=cv2.resize(char,(30,30))
                    
##                    plt.imshow(char,cmap="gray")
##                    plt.show()
                    i=j;
                    break;
                k+=1;
        else:
            i+=1;

    
    

