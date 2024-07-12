# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:20:05 2024

@author: Hp
"""

"""
x==3 is the scalar
x=[10,20,30] it is a vector in short single dimensional array called as vector
x=[[10,20,30],[10,20,30]] it is called as matrix and multidimentional array called as matrix
and when we are using multi times then it is called as tensors like
and more than 2 dimensional array called as tensor

x=[[[10,20],[20,30],[30,40]]]"""

import numpy as np
arr = np.array([[10,20,10,40],
                [40,50,70,90],
                [60,10,70,80],
                [30,90,40,30]])

x=arr[:3,::2]
print(x)

arr=np.arange(35).reshape(5,7)
print(arr)

#boolean indexing'

import numpy as np

arr=np.arange(12).reshape(3,4)
rows=np.array([False,True,True])

wanted_arr=arr[rows,:]
print(wanted_arr)

#conversion of array into the list
arr=np.array(list)
print(arr)



#numpy array Properties

#ndarray.shape
#ndarray.ndim
#ndarray.itemsize
#ndarray.size
#ndarray.dtype


#shape property of ndarray

array=np.array([[10,20,30],[20,30,40]])

array
print(array.shape)#(2, 3)

#reshaping of array is also possible in it

array.shape=(3,2)
print(array)
"""
[[10 20]
 [30 20]
 [30 40]]"""

array=np.array([[10,20,30],[20,30,40]])
new_arr=array.reshape(3,2)
print(new_arr)

