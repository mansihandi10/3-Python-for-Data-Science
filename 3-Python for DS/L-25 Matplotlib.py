# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:23:10 2024

@author: Matplotlib
"""

import matplotlib.pyplot as plt

X=range(1,20)
Y=[value*3 for value in X]

print("Value of X: ")
print(*range(1,20))
print("values of Y: ")
print(Y)
plt.plot(X,Y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Draw a line")

import matplotlib.pyplot as plt
#x axis values
x=[1,2,3]
y=[2,4,1]

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#setting a title
plt.title("Draw a line")

plt.plot(x,y)
#displaying of a graph
plt.show()

#to draw the two  or more line in the same graph

x1=[10,20,30]
y1=[40,10,30]

x2=[40,10,30]
y2=[10,20,30]

plt.plot(x1,y1,label="lin1")
plt.plot(x2,y2,label="lin2")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#setting a title
plt.title("Draw a line")
plt.legend()
plt.show()



#to draw the two  or more line in the same graph with diff colors and width

x1=[10,20,30]
y1=[40,10,30]

x2=[40,10,30]
y2=[10,20,30]

plt.plot(x1,y1,color="blue",linewidth=5,label="lin1")
plt.plot(x2,y2,color="red",linewidth=5,label="lin2")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#setting a title
plt.title("Draw a line")
plt.legend()
plt.show()



#to draw the two  or more line in the same graph with diff tyles

x1=[10,20,30]
y1=[40,10,30]

x2=[40,10,30]
y2=[10,20,30]

plt.plot(x1,y1,color="blue",linewidth=5,label="lin1",linestyle="dotted")
plt.plot(x2,y2,color="red",linewidth=5,label="lin2",linestyle="dashed")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#setting a title
plt.title("Draw a line")
plt.legend()
plt.show()
