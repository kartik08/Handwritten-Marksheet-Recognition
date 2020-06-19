#importing Keras, Library for deep learning 
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import  img_to_array
from keras import backend as K
K.set_image_dim_ordering('th')

import numpy as np

# Image manipulations and arranging data
import os
from PIL import Image
from sklearn.cross_validation import train_test_split
os.chdir("D:\Project\OCR only digits"); #folder that has the digits to used for training and testing.
#This folder should have 2 subfolders. 1 named testing_data and the other training_data

# input image dimensions
m,n = 30,30

path1="testing_data";
path2="training_data";

classes=os.listdir(path2)
x=[]
y=[]
for fol in classes:
    print (fol)
    imgfiles=os.listdir(path2+'\\'+fol);
    for img in imgfiles:
        im=Image.open(path2+'\\'+fol+'\\'+img);
        #im=im.convert(mode='RGB')
        imrs=im.resize((m,n))
        imrs=img_to_array(imrs)/255;
        imrs=imrs.transpose(2,0,1);
        imrs=imrs.reshape(1,m,n);
        x.append(imrs)
        y.append(fol)
        
x=np.array(x);
y=np.array(y);

batch_size=32
nb_classes=len(classes)
nb_epoch=20
nb_filters=32
nb_pool=2
nb_conv=3

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.2,random_state=4)

uniques, id_train=np.unique(y_train,return_inverse=True)
Y_train=np_utils.to_categorical(id_train,nb_classes)
uniques, id_test=np.unique(y_test,return_inverse=True)
Y_test=np_utils.to_categorical(id_test,nb_classes)

#Making the neural net
model= Sequential()
model.add(Convolution2D(nb_filters,nb_conv,nb_conv,border_mode='same',input_shape=x_train.shape[1:]))
model.add(Activation('relu'));
model.add(Convolution2D(nb_filters,nb_conv,nb_conv));
model.add(Activation('relu'));
model.add(Convolution2D(nb_filters,nb_conv,nb_conv));
model.add(Activation('relu'));
model.add(MaxPooling2D(pool_size=(nb_pool,nb_pool)));
model.add(Dropout(0.4));
model.add(Flatten());
model.add(Dense(128));
model.add(Dropout(0.4));
model.add(Dense(nb_classes));
model.add(Activation('softmax'));
model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])

#Training the net
nb_epoch=5;
batch_size=5;
model.fit(x_train,Y_train,batch_size=batch_size,nb_epoch=nb_epoch,verbose=1,validation_data=(x_test, Y_test))

#Testing the net
files=os.listdir(path1);
predictions=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#number of elements should be equal to number of char being detected
digits=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29] #same as above
for i in digits:
     
    img=files[i]        
    im = Image.open(path1 + '\\'+img);
    #im=im.convert(mode='RGB')
    imrs = im.resize((m,n))
    imrs=img_to_array(imrs)/255;
    imrs=imrs.transpose(2,0,1);
    imrs=imrs.reshape(1,m,n);
    x=[]
    x.append(imrs)
    x=np.array(x);
    predictions[i] = model.predict(x)

index=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # number of elements should be equal to number of char being detected
value=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # number of elements should be equal to number of char being detected

#Reading probability matrix 'predictions'
import xlsxwriter
for i in digits:
    a=predictions[i]
    a_max=max(a)
    max_value=max(a_max) #finding max of 1 probability array
    for j in range(0,10,1):
        if a_max[j]==max_value:
            max_index=j  
    index[i]=max_index #index has the char that have been detected

for i in digits:
    if i%2==0:
        num=index[i]*10;
    else:
        num=num+index[i]
        value[i]=num
        num=0
#writing in excel sheet
values=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #number of elements should be equal to half of number of char being detected
x=0
workbook=xlsxwriter.Workbook("Book.xlsx")
sheet=workbook.add_worksheet()
for i in range(0,30,2):
    values[x]=value[i]+value[i+1]
    sheet.write(x+1,0,values[x])
    x=x+1
workbook.close()   


