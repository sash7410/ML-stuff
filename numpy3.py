# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:41:29 2020

@author: sashank
"""

a = np.array ([[1,2,3,4],[7,8,2,0]])
print (np.min(a))
# axis = 0 is mins along column, axis = 1 is mins along each rows
print (np.min(a,axis=0))
print (np.min(a,axis=1))

#Mean of all emenents
b = np.array ([1,2,3,4,5,6])
m = sum (b)/5
print (m)
print (np.mean(b))
print (np.mean(a,axis=0)) #mean along columns

# Median or middle most value
c = np.array([1,5,4,2,0])
print (np.median(c))

# Mean vs average. avg is weighted
print (np.mean(c))

w = np.array ([1,2,3,4,5])
print (np.average(c,weights=w)) 

# Standard Deviation
u = np.mean(c)
myStd = np.sqrt(np.mean(abs(c-u)**2))
print(myStd)

#in built func for std deviation and variance
print (np.std(c))
print (np.var(c))