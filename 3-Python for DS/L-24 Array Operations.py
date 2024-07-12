# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:09:17 2024

@author: Hp
"""
    
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from numpy import array
l=[0.1,0.2,0.3,0.4]
#create an array
a=array(l)
#display of an array
print(a)
#display the shape of an array
print(a.shape)



data=array([11,22,33,44,55])
#index of data
print(data[4])
print(data[8])
"""IndexError: index 8 is out of bounds for axis 0 with size 5
"""
#hackerrank
#hackerer

from numpy import array
#define an array

data=array([[10,20,30],[40,50,60],[70,80,90]])
#we can also separtethe data
x,y=data[:,:-1],data[:,-1]
x
y

#bradcasting
from numpy import array

a=array([1,2,3,4])
print(a)#[1 2 3 4]
b=2
c=a+b
print(c)#[3 4 5 6]
#this will aad the element of b in each element of a 

#########################################################################
"""Vector l1 norm 
the l1 norm is calculated as the sum of the absolute vector values 
where the absolute vector values of ascalar uses the notation of |a1|
In the effect,the norm of Manhattan distance from the orgin of the vector
space """

from numpy import array
from numpy.linalg import norm
#define a vector array
a=array([1,4,6])
print(a)
#norm execute
l1=norm(a,1)
print(l1)

#L2 Norm
#define a vector array
a=array([1,2,3])
print(a)
#norm execute
l2=norm(a)
print(l2)

#traingular matrix

from numpy import array
from numpy import tril
from numpy import triu

M=array([[10,20,30],[40,50,60],[70,80,90]])

print(M)
lower=tril(M)

print(lower)
upper=triu(M)
print(upper)

##################################################
#diagonal matrix
from numpy import array
from numpy import diag

M=array([[10,20,30],[40,50,60],[70,80,90]])

d=diag(M)
print(d)

#transpose of the matrix
from numpy import array

A=array([[1,2],[2,3],[4,5]])

print(A)
C=A.T
print(C)

#inverse of matrix
from numpy import array
from numpy.linalg import inv

A=array([[1,2],[3,4]])
print(A)

#inverse matrix

B=inv(A)
print(B)

I=A.dot(B)
print(I)

#sparse matrix it is known as the more number of zeroes acress the element

from numpy import array
from scipy.sparse import csr_matrix

#to create dense matrix

A=array([[1,0,0,1,0,0],
         [0,0,2,0,0,1],
         [0,0,0,2,0,0]])

print(A)

s=csr_matrix(A)
print(s)
#to reconstruct the dense matrix
B=s.todense()
print(B)
