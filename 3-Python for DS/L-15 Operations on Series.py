# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:19:48 2024

@author: Hp
"""

#delettion of the Series

#del function is used
# del name_of_FataFrame[index]
import pandas as pd
s=pd.Series([4,5,6],index=(1,2,3))
del s[1]
s

#converting the datatypes
'''
string=use.astype(str)
numeric=use pd.to_numeric
ineteger=use astype(int)

this will fail with the Nan 
'''
import pandas as pd
s=pd.Series([3,None,11.0,9.0],index=['a','b','c','d'],name="Counts")
s.dtypes
#dtype('float64')

pd.to_numeric(s.apply(str)) 
#this will show the error coz the series also consisting of None Data type
#to avoid this error we use 'coerce' function
pd.to_numeric(s.apply(str),errors='coerce') 
s.dtypes

#to deal with this None function we can use this fillna function i.e
#DataFrame_name.fillna(-1)
s=s.fillna(-1)
s=s.astype(int) 
s.dtypes
#dtype('int32')

#Nan valuse also can be dropped by
#Data_Frame.dropna()
s=pd.Series([3,None,11.0,9.0],index=['a','b','c','d'],name="Counts")
s.dropna()
s 
#that row will be directly delted from the Series

#append, Combining and joing of two Series
import pandas as pd

s=pd.Series([3,None,11.0,9.0],index=['a','b','c','d'],name="Counts")
s1=pd.Series([7,16,21,39],index=['e','f','g','h'],name="Counts")
#to concatinate the two Series
s2=pd.concat([s,s1])

#plotting od Series

import matplotlib.pyplot as plt 
fig=plt.figure()
s2.plot()

plt.legend()

fig=plt.figure()
s1.plot(kind='bar')
s.plot(kind='bar', color='r')
plt.legend()

#histogram

import numpy as np
data=pd.Series(np.random.rand(500),name="500_random")
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
