# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:48:43 2020

@author: sashank
"""
a = np.arange (10) +5
print (a)

# Random functions

np.random.shuffle(a)
print (a)

# Returns values from standard normal distribution 
a = np.random.randn(2,3)
print (a)

# Returns values from standard something else lol distribution 
a = np.random.rand(2,3)
print (a)


# between 5 and 10 3 int numbers
a = np.random.randint(5,10,3)
print (a)

#starting number for rng everytime the code is run
np.random.seed(1)

#randomly pick one element from an array
elem = np.random.choice ([1,2,5,6,7])
print (elem)