# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:20:59 2024

@author: Hp
data types
operators
lits,dict and tuple
functions
lambda function

"""

#Python for Data Science
'''
Pandas: Series and Columns
Numpy
Matplotlib
Seaborn
'''
#series is used to manage the one dimentional data as similar to list in python
#the series object also having few more bits of data including and index and the name
import pandas as pd
s1=pd.Series([145,142,38,13],name="counts")
#it is very easy to inspect the index of a series
s1.index
#RangeIndex(start=0, stop=4, step=1)
#the index will be in the form of string and that that the datatype for the index are object
s1=pd.Series([145,142,38,13],name="counts",
             index=["a","b","c","d"])
s1.index
s1
"""
a    143
b    234
c    567
d    875
Name: counts, dtype: int64
"""

#numeric column will become the Nan value
import pandas as pd
f1=pd.read_csv("age.csv")
df=pd.read_excel("Bahaman.xlsx")
#None,Nan and null synonyms #the series object behaves similar to the numpy array
f1
"""     name   age
0       Ram  13.0
1      Sham  15.0
2  Ghansham   NaN"""
df
"""Defective     Country
0            0       India
1            0       India
2            0       India
3            0       India
4            1       India
..         ...         ...
795          0  Bangladesh
796          0  Bangladesh
797          1  Bangladesh
798          0  Bangladesh
799          0  Bangladesh

[800 rows x 2 columns]"""
import numpy as np
#they both having the methods 
numpy_ser=np.array([145,142,38,13])
s1[1]#142
numpy_ser[1]#142
s1.mean()#84.5
numpy_ser.mean()

#to create the series

george=pd.Series([10,7,1,22],index=["1999","1994","1996","1990"],name="George_Songs")
george
"""
1999    10
1994     7
1996     1
1990    22
Name: George_Songs, dtype: int64"""

#to read and select the data from the Series
george['1999']

for item in george:
    print(item)
    
#to update the values in the series

george["1994"]=78
george
