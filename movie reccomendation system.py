# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:03:45 2020

@author: sashank
"""


import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
#commaseperated value is csv
#tab seperated " is tsv
columns_names=["user_id","item_id","rating","timestamp"]

df= pd.read_csv("E:\codinngblocks ml course\ml-100k\ml-100k/u.data",sep='\t',names=columns_names)
print(df.head())
print(df.shape)
print(df['user_id'].nunique())
#unique item ids
print(df['item_id'].nunique())

movies_title=pd.read_csv("E:\codinngblocks ml course\ml-100k\ml-100k/u.item",sep='\|',header=None)
print(movies_title.shape)
movies_title=movies_title[[0,1]]
movies_title.columns=['item_id','title']

print(movies_title.head())
#JOINS DBMS SHIT(movies,df)
df1=pd.merge(df,movies_title, on="item_id")
print(df1.tail())
#%%%
#exploratory Data analysis
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
#print(df1.groupby('title').mean())
#avg of what makes sense??
#timestamp meh,user id meh,rating yesss

# groupby srranges based on the first column name and  .count() gives count of each column
#mean gives the mean of all values for the thing its grouped on like title
df1.groupby('title').mean()['rating']
#print(df1.groupby('title').mean()['rating'])
#sort in descending
df1.groupby('title').mean()['rating'].sort_values(ascending=False)

#print(df1.groupby('timestamp').mean()['rating'].sort_values(ascending=False))
print(df1.groupby('title').count()['rating'].sort_values(ascending=False))
rating =pd.DataFrame(df1.groupby('title').mean()['rating'])
print(rating.head())
#mean of ratings and count of ratings in num of ratings column
rating['numof ratings'] =pd.DataFrame(df1.groupby('title').count()['rating'])

print(rating.head())
#it could be possible that 5 star movies have only 1 user rating it
print(rating.sort_values(by='rating',ascending=False))

#plotit
plt.figure(figsize=(10,6))
#bins is inversely proportional to the width of blue line
#x axis -no of people who rated ,y axis no of movies watched(frequency of no of ppl who rated)
# like 900 movies were watched only by one person
#histogram plots frequency ig
plt.hist(rating['numof ratings'],bins =70 )
plt.show()