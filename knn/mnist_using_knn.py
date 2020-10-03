# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:01:04 2020

@author: sashank
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%%
df = pd.read_csv('E:/codinngblocks ml course/ML-stuff/knn/mnist_train.csv')
print(df.shape)#reshaped a 28*28 matrix image to 42000 rows

data =df.values#fn to convertt data frame into numpy array
print(data.shape)
print (type(data))
sheetx=data[:,1:]#drop the  first column as it has the digit value
sheety=data[:,0]#get teh first element in row (o/p)
print(sheetx.shape,sheety.shape)

split=int(0.8*sheetx.shape[0])#0.8 of 42k=33.6k
print(split)
x_train=sheetx[:split,:]#take first 33.6k rows and all columns
y_train=sheety[:split]#1d array so take 33.6k rows
#FIRST IS ROWS THEN COLUMNS LMAO
x_test=sheetx[split:,:]#same shit
y_test=sheety[split:]
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)

#%%%
def drawimg(sample):
        img=sample.reshape((28,28))
        plt.imshow(img,cmap='gray')
        plt.show()
        
drawimg(x_train[3])
print(y_train[0])


#%%%
def dist(x1,x2):
        return np.sqrt(sum((x1-x2)**2))
def knn(sheetx,sheety,querypt,k=5):
    
    vals=[]
    m=sheetx.shape[0]
    
    for i in range(m):
            d=dist(querypt,sheetx[i])
            vals.append((d,sheety[i]))
            #append distance and sheety val 0 or 1
            #sort
    vals=sorted(vals)
    vals=vals[:k]
    vals=np.array(vals)#converting python list to array
    #nearest first k points
    new_vals=np.unique(vals[:,1],return_counts=True)
    print(new_vals)
    
    index=new_vals[1].argmax()
    pred=new_vals[0][index]
    return pred
#%%%
c=0
for i in range (5):
    pred=knn(x_train,y_train,x_test[i])
    lol=int(pred)
    lol1=y_test[i]
    """ print(int(pred))
     
     drawimg(x_test[i])
     print(y_test[i])"""
    if lol==lol1 :
        c+=1
print (c/5)#accuracy