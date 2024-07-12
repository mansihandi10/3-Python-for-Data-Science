# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:07:49 2024

@author: Hp
"""

#Matplotlib is widely used in the EDA(Exploratory Data Analysis)
#in Data Science we have to first "undertsnading the business problem"

#introducing markers in the graph

import matplotlib.pyplot as plt

#x axis values
x=[1,4,5,6,7]
#y-axis values
y=[2,6,3,6,3]

#plotting the points

plt.plot(x,y,color="red",linestyle="dashdot",linewidth=3,marker="o",
         markerfacecolor="blue",markersize=12)

#set the y-limits of curreng axes
plt.ylim(1,8)
#set the x-limits of curreng axes
plt.xlim (1,8)
plt.title("Display Marker")
plt.show()

#write a python program to display a bar graph showing the popularity of programming language

import matplotlib.pyplot as plt
x=["Java","Python","PHP","JS","C","C++"]
popularity=[98,85,80,50,40,30]

x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color="red")
plt.xlabel("languages")
plt.ylabel("Popularity")
plt.xticks(x_pos,x)
#to turn on the grid
plt.minorticks_on()
plt.grid(which="major",linestyle="-",linewidth="0.5",color="blue")
plt.show()

import matplotlib.pyplot as plt
x=["Java","Python","PHP","JS","C","C++"]
popularity=[98,85,80,50,40,30]

x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color="red")
plt.xlabel("languages")
plt.ylabel("Popularity")
plt.yticks(x_pos,x)
#to turn on the grid
plt.minorticks_on()
plt.grid(which="major",linestyle="-",linewidth="0.5",color="blue")
plt.show()

import matplotlib.pyplot as plt
x=["Java","Python","PHP","JS","C","C++"]
popularity=[98,85,80,50,40,30]

x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=["red","black","yellow","cyan","green","orange"])
plt.xlabel("languages")
plt.ylabel("Popularity")
plt.xticks(x_pos,x)
#to turn on the grid
plt.minorticks_on()
plt.grid(which="major",linestyle="-",linewidth="0.5",color="blue")
plt.show()

#Histogram

import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80]
plt.hist(blood_sugar,rwidth=0.8)
plt.hist(blood_sugar,rwidth=0.5,bins=4)

###########################################################################

#BoxPlot
import matplotlib.pyplot as plt
import numpy as np
#creating a random dataset
np.random.seed(10)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7))
#creating the plot
plt.boxplot(data)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
#creating a random dataset
np.random.seed(10)
d1=np.random.normal(100,20,200)
d2=np.random.normal(90,20,200)
d3=np.random.normal(80,30,200)
d4=np.random.normal(70,40,200)
data=[d1,d2,d3,d4]
fig=plt.figure(figsize=(10,7))
#creating the plot
ax=fig.add_axes([0,0,1,1])

bp=ax.boxplot(data)
plt.show()