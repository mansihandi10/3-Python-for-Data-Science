# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:05:47 2024

@author:  Mansi Balram Handi
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

#select the rows by using labels
#loc is only used when we are selecting the rows by using labels

df2=df.loc[['r1']]
df2=df.loc[['r1','r4','r5']]

#by using df[] notations

df2=df['Courses']
#by select the multiple columns

df2=df[['Courses','Fees','Duration']]
#by using the loc to take the column slices
#loc[] syntax to slice columns
#df.loc[:,start,end,step]

#select any random columns
df2=df.loc[:,["Courses","Fees","Duration"]]
#select columns between two columns
df2=df.loc[:,"Fees":"Discount"]
#all columns upto the duration
df2=df.loc[:,:"Duration"]
df2=df.loc[:,::2]

#Pandas.DataFrame.query() by example

df2=df.query("Courses=='Spark'")
df2

#not equal conditions
df2=df.query("Courses!='Spark'")
df2


#to add the column in the DataFrame

tutors=["A","B","C","D","E","F","G","H"]
df2=df.assign(TutorsAssigned=tutors)
df2

#Derive column from Existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_percent=lambda x:x.Fees*x.Discount/100)
df2

#we can also add the specific position

df=pd.DataFrame(technologies)
df.insert(0,"Tutors",tutors)
df
"""
  Tutors Courses     Fees Duration  Discount
0      A   Spark  20000.0  30 Days        10
1      B  Pandas  30000.0                 11
2      C  Hadoop  40000.0  30 Days        12
3      D  Oracle      NaN  30 Days        13
4      E    Java  50000.0  30 Days        15
5      F    None  60000.0  30 Days        16
6      G  Python  70000.0  30 Days        17
7      H   Numpy  80000.0  30 Days        18"""

#to renameing the multiple columns
import pandas as pd
import numpy as np

technologies={
    "Courses":["Spark","Pandas","Hadoop","Oracle","Java",None,"Python","Numpy"],
    "Fees":[20000,30000,40000,np.nan,50000,60000,70000,80000],
    "Duration":["30 Days"," ","30 Days","30 Days","30 Days","30 Days","30 Days","30 Days"],
    
    }
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
df

df2=df.rename(columns={"Courses":"Courses_list"})
df2
df2.columns

df2=df.rename(columns={"Courses":"Courses_list","Fees":"Amount_to_pay","Duration":"Peroid_of_Course"},inplace=True)
df2
df2.columns