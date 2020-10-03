# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:27:08 2020

@author: sashank
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfx = pd.read_csv('E:/codinngblocks ml course/ML-stuff/knn/xdata.csv')
dfy = pd.read_csv('E:/codinngblocks ml course/ML-stuff/knn/ydata.csv')
sheetx=dfx.values
sheety=dfy.values
print(sheetx)
sheetx=sheetx[:,1:]
#without reshap it will be n*1 matrix we need a 1*n matrix so reshape
sheety=sheety[:,1:].reshape((-1,))
print(sheetx)
print(sheety)
print(sheetx[:,0])
print(sheetx[:,1])
#this graph is plotted like x-cord=1st column ofsheetx and
#y-cord is the 2nd column of sheetx plt.scatter(x.cord,y.cord)
#the colout is based on the calue of the same index in excel sheetY
plt.scatter(sheetx[:,0],sheetx[:,1],c=sheety)
plt.show()
query_x= np.array([0,0])
plt.scatter(sheetx[:,0],sheetx[:,1],c=sheety)
#plot at x=2 and y=3
plt.scatter(query_x[0],query_x[1],color='red')

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

x=knn(sheetx,sheety,query_x)
print(x)