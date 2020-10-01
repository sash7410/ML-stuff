import numpy as np

# tensor is an array with more than 2 axes (3d matrix)

T = np.ones((2,3,2))  
print (T) 

# tensor can be used to store images 
# images are represented by a 3d array/ tensor of RGB
# (255,255,255) is white and (0,0,0) is black

import matplotlib.pyplot as plt

black = np.zeros((5,5,3),dtype = 'uint8') 

plt.imshow(black)
plt.show()   

#%%%
#slicling all rows, all columns and only 0th channel, i.e, red
black = np.zeros((5,5,3),dtype = 'uint8') 
black[: , : ,1] = 255 
plt.imshow(black)  
plt.show() 

#1st and 2nd channel are green and blue
#black = np.zeros((5,5,3),dtype = 'uint8') 
black[: , : ,0] = 255 
plt.imshow(black)  
plt.show() 

#black = np.zeros((5,5,3),dtype = 'uint8') 
black[:, :,2] = 255
plt.imshow(black)  
plt.show() 


#%%%
# Transpose of a vector and array
x = np.array([[1],[2],[3],[4]])
print (x)
print (x.T ,"\n")  
 

y =x.reshape(2,-1)
print (y)
print (y.T, "\n") 


# Transpose of a tensor
a = np.zeros ((25,50,3))
print (np.shape(a)) 

b = np.transpose(a)
print (np.shape(b))

c = np.transpose(a,axes= (2,0,1))
print (np.shape(c))

d = np.transpose(a,axes= (1,0,2))
print (np.shape(d),"\n")


#%%%
# Broadcasting - adding a scalar to a vector 
# scalar will be added to every element in the vector

x = np.array([1,2,3,4])
print (x)
print (x+5, "\n") 

#vector + matrix = vector is added to corres. column of matrix

y = np.array ([[1,2,3,4],
               [1,2,3,4]])

print (x+y) 

#%%%
#Element wise multiplication of matrices

a = np.array ([[1,2],
               [1,2]])

b = np.array ([[1,2],
               [0,0]])

print ((a*b) ,"\n" )

# Dot product / matric multiplication

print (np.dot(a,b)) 


#%%%
# Norms 
#Lp norm, L2 norm, L1 norm

# Lp2 norm = (2^2 + 3^2) ^ (1/2)
# Lp1 norm = (2^1 + 3^1) ^ (1/1)

x = np.array ([2,3])

lp2 = np.linalg.norm(x)
print (lp2, "\n")

lp1 = np.linalg.norm(x,ord=1)
print (lp1, '\n')

# L infinity norm = Abs value of highest magnitude element
l_inf = np.linalg.norm(x,ord=np.inf) 
print (l_inf, "\n") 

#Properties of norms
# Norm is func that maps vectors to non negative values
# If x is the vector, then norm is a func of x or f(x)
# if f(x)= 0, then x is a zero vector
# f (x+y) always <= f(x) + f(y)
# f (a.x) = abx(a). f(x) where a is a real number
 

#%%%
# Determinants 
a = np.array ([[1,2],
               [3,4]])

print (np.linalg.det(a)) 

# Inverse of a matrix
# a . inv(a)  = identity matrix
# if det of a matrix is zero, inv doesnt exist
# pseudo inv can be used if det is zero

print (np.linalg.inv(a) , "\n")  
print (np.dot(a,np.linalg.inv(a)) , "\n") 

b = np.array ([[6,8],
               [3,4]])

# if det isnt zero then pinv = inv

print (np.linalg.det(b))
print (np.linalg.pinv(b) , "\n")  


#%%%
# Solving linear matrix eqns or system of linear scalar eqns

# 1.x1 + 2 = 10
# 3.x2 + 4 = 20
# A . X = B
# [[1 2]  [[x1]   = [[10]
# [3 4]]   [x2]]     [20]]


a = np.array ([[1,2],
               [3,4]])

b = np.array ([10,20])

print (np.linalg.solve(a,b) )



