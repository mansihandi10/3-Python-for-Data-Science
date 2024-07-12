# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:12:41 2024

@author: Hp
"""

import pandas as pd
import numpy as np
technologies={
    "Courses":["Spark","Pandas","Hadoop","Oracle","Java",None,"Python","Numpy"],
    "Fees":[20000,30000,40000,np.nan,50000,60000,70000,80000],
    "Duration":["30 Days"," ","30 Days","30 Days","30 Days","30 Days","30 Days","30 Days"],
    "Discount":[10,11,12,13,15,16,17,18]
    }

df=pd.DataFrame(technologies)
df
df.to_excel("Courses.xlsx")

df=pd.read_excel("Courses.xlsx")
df

#using Series.values.tolost()

col_list=df.Courses.values
col_list
"""array(['Spark', 'Pandas', 'Hadoop', 'Oracle', 'Java', nan, 'Python',
       'Numpy'], dtype=object)"""

col_list=df.Courses.values.tolist()
col_list
"""['Spark', 'Pandas', 'Hadoop', 'Oracle', 'Java', nan, 'Python', 'Numpy']"""

#by using list function

col_list=list(df["Courses"])
col_list
"""['Spark', 'Pandas', 'Hadoop', 'Oracle', 'Java', nan, 'Python', 'Numpy']"""

#differencxe between array and list
"""
array can store homogenoues entities means it can only store single type of datatypes
and the list can store heterogenoues entities means it can store any type of datatypes"""

'''
python list can contain differrnt datatypes within a single list,
all of the elements in a Numpy array should be homogeneous 
'''
#Array In Numpy
# create np array
import numpy as np
arr = np.array([10,20,30])
print(arr)
####################################################################
#[]- single dimensinal array
#[[]]- two dimensinal array
#[[[]]]--Multidimenal  / three

#Multidimensional array
arr = np.array([[10,20,30],[10,20,30]])
print(arr)
'''
print(arr)
[[10 20 30]
 [10 20 30]]
'''
######################################################################
arr = np.array([10,20,30,40],ndmin = 3)
print(arr)

#print(arr)
#[[[10 20 30 40]]]

######################################################################
#chnage the data type 
#dtype parameter 

arr = np.array([10,20,30],dtype =complex)
print(arr)

#[10.+0.j 20.+0.j 30.+0.j]

#Get dimension of the array 
arr= np.array([[1,2,3,4],[7,8,9,10],[11,12,13,14]])
print(arr.ndim)
print(arr)

#print(arr.ndim)
#2
#print(arr)
#[[ 1  2  3  4]
 #[ 7  8  9 10]
 #[11 12 13 14]]
 
 #finding the size of each item in the array 
arr =np.array([10,20,30])
print("Each item is of the type", arr.dtype)

#get the shapwe and size of the array 
arr = np.array([[10,20,30,40],[50,60,70,80],[11,12,13,14]])
print("Array size :-",arr.size)
print("Array shape :-",arr.shape)
#Creating array from list with type float
arr = np.array([[1,2,3],[4,5,6]],dtype=float)
print(arr)
#####################################################################
#create a sequence of interger using arrange()
#create a sequence of integer
# from 0 to 20 with steps of 3 
arr= np.arrange(0,20,3)
print("A sequential array with steps of 3:\n", arr)

###################################################################
#Access single element using index
arr =np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[2])
#2
print(arr[-4])

arr = np.array([[10,20,30],[40,50,60]])
print(arr)
print(arr.shape)

print(arr[1,2])
print(arr[0,2])

print(arr[1,-1])
#access aray elements with the help of slicing

arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)
#[2 4 6 8]

x=arr[-2:3:-1]
x

x=arr[-2:10]
x

#slicing in multidimentional array
arr = np.array([[10,20,10,40],
                [40,50,70,90],
                [60,10,70,80],
                [30,90,40,30]])

arr

arr[1,3]# 90
arr[1,:]#array([40, 50, 70, 90])
arr[:,1]#array([20, 50, 10, 90])
