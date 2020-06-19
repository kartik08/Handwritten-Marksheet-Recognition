import cv2
def binarization(img):
    ret,img=cv2.threshold(img,0,1,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return img
def binarization1(img):
    ret,img=cv2.threshold(img,0,1,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img
