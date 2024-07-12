# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 08:15:20 2024

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
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
df

#dataFrame Propertes
df.shape#(8, 4)
df.size#32
df.columnsI#ndex(['Courses', 'Fees', 'Duration', 'Discount'], dtype='object')
df.columns.values#array(['Courses', 'Fees', 'Duration', 'Discount'], dtype=object)
df.index#Index(['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7'], dtype='object')
df.dtypes
'''
Courses      object
Fees        float64
Duration     object
Discount      int64
dtype: object'''
df.info

#accesing the column by name

df["Fees"]
'''
r0    20000.0
r1    30000.0
r2    40000.0
r3        NaN
r4    50000.0
r5    60000.0
r6    70000.0
r7    80000.0
Name: Fees, dtype: float64'''


#acces two columns at a time

df[["Fees","Duration"]]
"""
       Fees Duration
r0  20000.0  30 Days
r1  30000.0         
r2  40000.0  30 Days
r3      NaN  30 Days
r4  50000.0  30 Days
r5  60000.0  30 Days
r6  70000.0  30 Days
r7  80000.0  30 Days"""

#we can also accces two columns by another method then we will get the same result

cols=["Fees","Duration"]
df[cols]
df[["Fees","Duration"]]
"""
       Fees Duration
r0  20000.0  30 Days
r1  30000.0         
r2  40000.0  30 Days
r3      NaN  30 Days
r4  50000.0  30 Days
r5  60000.0  30 Days
r6  70000.0  30 Days
r7  80000.0  30 Days"""

#to acces the rows
df[6:]
''' Courses   Fees     Duration  Discount
r6  Python  70000.0  30 Days        17
r7   Numpy  80000.0  30 Days        18'''

#accessing specific cell from the column
df["Duration"][5]
#'30 Days'

df[:6,]

#substrating or adding specofic value from coumn

df["Fees"]=df["Fees"]-200
df["Fees"]
"""
r0    19800.0
r1    29800.0
r2    39800.0
r3        NaN
r4    49800.0
r5    59800.0
r6    69800.0
r7    79800.0
Name: Fees, dtype: float64"""

df.describe()#5 number summary 
#used to describe teh DataFrame only for numeric values
'''
               Fees  Discount
count      7.000000    8.0000
mean   50000.000000   14.0000
std    21602.468995    2.9277
min    20000.000000   10.0000
25%    35000.000000   11.7500
50%    50000.000000   14.0000
75%    65000.000000   16.2500
max    80000.000000   18.0000'''


#renaming of the columns in the DataFrame

df=pd.DataFrame(technologies,index=row_labels)
df
df.columns=["A","B","C","D"]
df
df.columns=["c1","c2","c3","c4"]
df


# it also having another way to rename it

df.columns=["A","B","C","D"]
df2=df.rename({"A":"c1","B":"c2"},axis=1)
df2=df.rename({"C":"c3","D":"c4"},axis="columns")
df2=df.rename(columns={"A":"c1","B":"c2"})
#this method is used only when we want to rename specific name of the columns


#Drop rows and Columns from the DataFrame

df1=df.drop(["r1","r2"])



import pandas

df=pandas.DataFrame(technologies)
df
