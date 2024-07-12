# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:22:11 2024

@author: Hp
"""

#Dataframe:
'''It is the two dimentionaal data structure and it is immutatble
(we can't play woth this') data structure with labreled axes rows and 
columns
'''
#this is also a one command to install padas

#conda install pandas
#Feachers of DataFrame
import pandas as pd
pd.__version__
#'2.0.3'

#to create the Dataframe the we have to write a code of list inside the list
Technoligies=[["Spark",40000,"40 Days"],
              ["Pandas",40000,"40 Days"]]
df=pd.DataFrame(Technoligies)
df
""" 
       0      1        2
0   Spark  40000  40 Days
1  Pandas  40000  40 Days
"""
#by default it will give tje indexes and name of columns as 0,1,2,3 and so on

#yo assign the names of columns and indexes
column_name=["Course","Fees","Duration"]
Row_label=["a","b"]
df=pd.DataFrame(Technoligies,columns=column_name,index=Row_label)

df
'''Course   Fees Duration
a   Spark  40000  40 Days
b  Pandas  40000  40 Days'''
df.dtypes
'''
Course      object
Fees         int64
Duration    object
dtype: object'''


#to create DataFrame using Dictionary
# to assign column names and the indexes ro te data we can also use dictionary
# it is thye standard method
import pandas as pd

technologies={
    "Courses":["Spark","Pandas","Hadoop","Oracle","Java"],
    "Fees":[20000,30000,40000,50000,60000],
    "Duration":["30 Days","30 Days","30 Days","30 Days","30 Days"],
    "Discount":[10,11,12,13,15]
    }
df=pd.DataFrame(technologies)
df
"""  Courses   Fees Duration  Discount
0   Spark  20000  30 Days        10
1  Pandas  30000  30 Days        11
2  Hadoop  40000  30 Days        12
3  Oracle  50000  30 Days        13
4    Java  60000  30 Days        15"""

df.dtypes
'''
Courses     object
Fees         int64
Duration    object
Discount     int64
dtype: object
'''
#ro convert all the datatypes into best possible dtypes
df2=df.convert_dtypes()
df2
df2.dtypes
#if we want all the datatypes to the same dtypes
df=df.astype(str)
df.dtypes
'''Courses     object
Fees        object
Duration    object
Discount    object
dtype: object'''


#to changr the type for one or more multiple columhns
df=df.astype({"Fees":int,"Discount":float})
df.dtypes
"""

Courses     object
Fees        object
Duration    object
Discount    object
dtype: object"""

# to convert datatypes for all the columns in a list

df=pd.DataFrame(technologies)
df.dtypes

cols=["Fees","Discount"]
df[cols]=df[cols].astype('float')
df.dtypes
df

# to ignore errors if sometimes we make mistakes 

df=df.astype({"Courses":int},errors='ignore')
df.dtypes
"""
Courses      object
Fees        float64
Duration     object
Discount    float64
dtype: object"""
#if we want to raise an error as per
df=df.astype({"Courses":int},errors='raise')

#to convert the datatype into the numeric
df.astype(str)
df["Discount"]=pd.to_numeric(df["Discount"])
#when we use the to nuemric form iit wil only convert the list into the
#FLOAT form
df.dtypes
'''Courses      object
Fees          int32
Duration     object
Discount    float64
dtype: object'''


#dataframe to dictionary

import pandas as pd

technologies={
    "Courses":["Spark","Pandas","Hadoop"],
    "Fees":[20000,30000,40000],
    "Duration":["30 Days","30 Days","30 Days"],
    "Discount":[10,11,12]
    }

df=pd.DataFrame(technologies)
df
#convert DataFrame into the csv file
df.to_csv("data_file.csv")
#to create DataFrmae from 
df=pd.read_csv("data_file.csv")
df


#Pandas DataFrame

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

df.to_csv("data_file2.csv")

'''   Courses     Fees Duration  Discount
r0   Spark  20000.0  30 Days        10
r1  Pandas  30000.0                 11
r2  Hadoop  40000.0  30 Days        12
r3  Oracle      NaN  30 Days        13
r4    Java  50000.0  30 Days        15
r5    None  60000.0  30 Days        16
r6  Python  70000.0  30 Days        17
r7   Numpy  80000.0  30 Days        18'''