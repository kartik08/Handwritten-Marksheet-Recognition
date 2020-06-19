import numpy as np
import matplotlib.pyplot as plt
import cv2
from charseg import charseg
def corner(img,img1):
    [x,y]=img.shape
    for i in range(0,x-4):
        if img[i][50]==1 and img[i+1][50]==0:
                for j in range(i,x-4):
                    if img[j][50]==0 and img[j+1][50]==1:
                        a=img1[i:j,:]
                        for k in range(0,y-9):
                            if img[15][k]==1 and img[15][k+1]==0:
                                for l in range(k,y-9):
                                    if img[15][l]==0 and img[15][l+1]==1:
                                        b=a[:,k:l]
                                        [r,c]=b.shape
                                        b[0:3,:]=0;
                                        b[r-3:r,:]=0
                                        b[:,0:3]=0;
                                        b[:,c-3:c]=0;
                                        
                                        charseg(b)
                                        break;
                        break;
        
                    
            
    return
                
                                        
                    
                    
    
         
