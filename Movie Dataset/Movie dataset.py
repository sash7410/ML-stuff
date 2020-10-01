# Scatter plot between length of title and no of movies
# Scatter plot between 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

#%%%
df = pd.read_csv("D:\Python\Movie Dataset\movie_metadata.csv") 

print (df.head(n=3) )
print (df.columns)

titles = list (df.get('movie_title'))
scores = list (df.get('imdb_score'))

freq_title = {}



for t in titles:
    length = len(t)
    
    #Dictionary keys can be accessed by []
    
    try:
        freq_title[length] +=1
    except:
        freq_title[length] = 1

print (freq_title)

x = np.array(list(freq_title.keys()))
y = np.array(list(freq_title.values()))

plt.scatter(x,y)
plt.xlabel ("Movie title length")
plt.ylabel ("No of movies")
plt.show()


#%%%
freq_score = {}

for s in scores:
    try:
        freq_score[s] +=1
    except:
        freq_score[s] = 1
    
print (freq_score) 

a = np.array(list(freq_score.keys()))
b = np.array(list(freq_score.values()))

plt.scatter(a,b)
plt.xlabel ("Imdb Score")
plt.ylabel ("No of movies")
plt.show()































