import cv2
def contrast(img1):
    lab= cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)

#-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)

#-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)


#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))

#-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    final = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
    return(final)
