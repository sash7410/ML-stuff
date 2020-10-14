# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:51:43 2020

@author: sashank
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
X=pd.read_csv('./Training_Data/Linear_X_Train.csv')
y=pd.read_csv('./Training_Data/Linear_Y_Train.csv')

#convert X,y to Numpy array
X=X.values
y=y.values

#normalisation
u=X.mean()
std=X.std()
X=(X-u)/std

plt.scatter(X,y)
print(X.shape,y.shape)

#theta[0]=c theta[1]=m(slope)
def hypothesis(x,theta):
    y_ =theta[0] + theta[1]*x #y=mx+c
    return y_

def gradient(X,Y,theta):
    m=X.shape[0]
    grad=np.zeros((2,))#n*2 matrix i guess
    for i in range(m):
        x=X[i]
        y_=hypothesis(x,theta)
        y=Y[i]
        grad[0]+=(y_-y)
        grad[1]+=(y_-y)*x
        
    return grad/m#divides both the gradients 0,1

def error(X,Y,theta):
    m=X.shape[0]
    total_error=0.0
    for i in range(m):
        y_=hypothesis(X[i],theta)
        total_error+=(y_ -Y[i])**2
    return total_error/m

def gradientDescent(X,Y,max_steps=100,learning_rate=0.1):
    theta=np.zeros((2,))
    error_list =[]
    for i in range(max_steps):
        #compute grad
        grad=gradient(X,Y,theta)
        e=error(X,Y,theta)
        error_list.append(e)
        #update theta
        theta[0]=theta[0]-learning_rate*grad[0]
        theta[1]=theta[1]-learning_rate*grad[1]
    return theta,error_list
    
theta,error_list=gradientDescent(X, y)
print(error_list)
plt.plot(error_list)
    
    