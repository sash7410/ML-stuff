# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:25:40 2020

@author: sashank
"""
#math operations
import numpy as np
a=np.array([1,2,3,4])
print (a)
print(type(a))
print (a.shape)
b=np.array([[1],[2],[3],[4]])
print(b)
print(b.shape)
c=np.array([[1,2],[3,4]])
print(c)
print(c.shape)

a=np.zeros((3,3))
print(a)

b=np.ones((2,3))
print(b)
c=np.full((3,2),5)
print(c)

d=np.eye(4)#identity matrix
print(d)
#random matrix for neural networks
randomMatrix=np.random.random((2,3,5))
print(randomMatrix)
print(randomMatrix[0,0,0])

#slicing
randomMatrix=np.random.random((2,3))
print(randomMatrix)
print(randomMatrix[:,2])

z=np.zeros((3,3))
print(z)
z[1,:]=5
z[:,-1]=7
print(z)

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print(x+y)
print(np.add(x,y))
print(x-y)
print(x*y)
print(np.multiply(x,y))
print(x/y)
print(np.divide(x,y))

 #matrix multiplaction
print(x.dot(y))
print(np.dot(x,y))

#multiplication of vectors(dot)->scalar
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
print(a.dot(b)) #30
print(a)
print(sum(x))
print(np.sum(x))
print(np.sum(x,axis=1))#0is vertical sum 1 is horizontal

#stacking of arrays(makes it as a 2d matrix)
print(a)
b=b**2
print(b)
z=np.stack((a,b),axis=1)
print(z)
z=np.stack((a,b),axis=0)
print(z)

#reshape
z=z.reshape((4,2))
print(z)
"""
z=z.reshape((4,3))
print(z)
wont work as size =8
"""