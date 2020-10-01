#MNIST
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("D:\Python\MNIST\mnist_data.csv") 

print (df.shape) 

#   print (df.head(n=1)) 

data = df.values #Convert to numpy array

# Randomizing data for good distribution in test and training sets
# Randamizing rows to remove uniformity in data in training and test 
np.random.shuffle(data)

#Separate X and Y values
#Y is a column matrix
#Each scalar in Y denotes the label for an image
#Each row in X denotes one image (pixel values for each label)


X = data [ : ,1: ]
Y = data [ : ,0]

print (Y.shape,"\n", X.shape) 
 
#%%%
# Visualizing one image

def drawImg(X,Y,i):
    plt.imshow(X[i].reshape(28,28) , cmap="gray")
    plt.title("Label: " + str(Y[i]))
    plt.show()

for i in range(5):
    drawImg(X,Y,i)  

#%%%
#Splitting this data set 
#One for training the algorithm
#One for testing/validation

# 80% for training
split = int (0.80 * X.shape [0])

print (split) 

X_train, Y_train = X[ :split, :] , Y[:split] 
X_test, Y_test = X[split: , :] , Y[split: ]

print (X_train.shape, Y_train.shape)
print (X_test.shape, Y_test.shape)

# Plot a visualization 
# 25 grid - 5 x 5 images
# plt.subplot is used to make a 5 x 5 grid where images are plotted
# the grids are numbered from 1-25. hence i+1 since for loop starts from 0

plt.figure(figsize=(10,10))
for i in range (25):
    plt.subplot(5,5,i+1)
    plt.imshow(X_train[i].reshape(28,28) ,cmap="gray")
    plt.title(Y_train[i])
    plt.axis("off")  #turns off axes in the images

#In built func to do test and training split
#%%%
from sklearn.model_selection import train_test_split

#The func does shuffling everytime the code is run
#To get the same split, random_state is used (its like a seed value)

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y,test_size=0.2 ,random_state=5)
print (Xtrain.shape, Ytrain.shape)
print (Xtest.shape, Ytest.shape)




