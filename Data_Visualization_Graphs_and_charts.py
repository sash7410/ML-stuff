#Data Visualization 
#%%%

import matplotlib.pyplot as plt
import numpy as np

themes = plt.style.available
print (themes) 
 
# Line plot

x = np.arange(10)
y1 = x**2
y2 = 2*x + 3

#plot (x axis, y axis)
# if one one axis is given, itll be taken as y axis. the x axis will be the indices of the matrix
plt.plot(x,y1)
plt.show()  

plt.style.use("classic")
plt.plot(x,y1)
plt.show()

#plot.show can be used to separate two diff plots as well
plt.style.use("seaborn-white")
plt.plot(x,y1,color='red', label="A")
plt.plot(x,y2,color='green', label="B", linestyle="dashed", marker="o")
plt.xlabel("Time")
plt.ylabel("Cost")
plt.title("Cost vs time") 
plt.legend() 
plt.show() 

#%%%
#Scatter Plot

#Adjusting size of plot
plt.figure(figsize=(10,6))

plt.scatter(x,y1,color='red', label="A", marker="+")
plt.scatter(x,y2,color='green', label="B", marker="o") 
plt.xlabel("Time")
plt.ylabel("Cost")
plt.title("Cost vs time scatter") 
plt.legend() 
plt.show() 



#%%%
#Bar graphs
plt.bar([1,2,3],[15,25,30])
plt.bar([1,2,3],[10,20,15])
plt.show()  #Overlapping

x_coord = np.array([1,2,3])
plt.bar(x_coord,[15,25,30], width=0.5)
plt.bar(x_coord+0.5, [10,20,15],width=0.5)
plt.show() 

plt.style.use("dark_background")
x_coord = np.array([1,2,3]) * 2
plt.bar(x_coord - 0.25,[15,25,30], width=0.5, label="A", tick_label=["1","2","3"], color="blue")
plt.bar(x_coord + 0.25, [10,20,15],width=0.5, label = "B", color="green")
plt.xlabel("Time")
plt.ylabel("Cost")
plt.ylim(0,40)
plt.legend()
plt.show() 

#%%%
# Pie Chart

s = "a","b","c","d"
weightage = [20,10,40,30]

plt.pie(weightage,labels=s)
plt.show()

plt.style.use("seaborn-white")
plt.pie(weightage,labels=s, explode=(0,0,0.2,0), autopct='%1.1f%%',shadow=True, colors=["pink","green","blue","yellow"])
plt.show()


#%%%
# Normal Distribution
# Std normal distribution

# Histogram

xsn = np.random.rand(100)
print (xsn)

sigma = 5 #std deviation about mean (how spread out a group of numbers is from the mean,)
u = 70 #Mean value 
x = np.round(xsn*sigma +u)
x2 = np.round(xsn*3 + 65)
print (x) 




plt.style.use("seaborn")
plt.hist(x,alpha=0.8,label="A")  #alpha is opacity
plt.hist(x2, alpha=0.8,label="B")
plt.ylabel("Freq/number of people in range")
plt.title("histogram")
plt.show() 









