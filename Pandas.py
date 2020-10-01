# PANDAS

#Dataframe - special object to store data in tabular form

import numpy as np
import pandas as pd

#%%%
#Creating a dataframe
data = {
        "A": np.random.randint(1,100,5),
        "B": np.random.randint(50,100,5),
        "C": np.random.randint(1,100,5)
            }
    
print (data) 

df = pd.DataFrame(data,dtype='int8')  #data type is optional
print (df , "\n") 

print (df.head(n=2), "\n")
print (df.tail(n=2), "\n") 

print (df.columns)

df.to_csv('E:\codinngblocks ml course/data1.csv')  #Creates a csv file

data = pd.read_csv('E:\codinngblocks ml course/data1.csv') 
print (data) 

data = pd.read_csv('E:\codinngblocks ml course/data1.csv') 
data =data.drop(columns=['Unnamed: 0'])
print (data) 


#To remove that unnamed column directly from csv
df.to_csv('E:\codinngblocks ml course/data2.csv',index=False)

new_data = pd.read_csv ('E:\codinngblocks ml course/data2.csv')
print ("\n", new_data)



#%%%
print (data.describe(),"\n")

# Accessing row
print (data)
print (df.iloc[3] , "\n") #accessing 3rd row

#Accessing row and column
print (df.iloc[3,1])

#If index value isnt known

idx = df.columns.get_loc("B")
print (idx)
print (df.iloc[3,idx])

idx = [df.columns.get_loc("B"), df.columns.get_loc("C") ]
print (df.iloc[:3,idx])

print (df.iloc[:3, 0:2])

#%%%
# Sorting the data
print (data.sort_values(by=["A"],ascending=False))


#%%%
# Creating an array from data
array = data.values
print (array)

#NumPy array to dataframe
new_df = pd.DataFrame(array,dtype='int32',columns=["X","Y","Z"])
print (new_df)







