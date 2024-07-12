# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:38:47 2024

@author: Mansi Handi
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

#drop down the column by using index

print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)
df
#using inplace True

df.drop(df.columns[2],axis=1,inplace=True)
df

df=pd.DataFrame(technologies)
#drop two or more columns by using label name
df2=df.drop(["Courses","Fees"],axis=1)
df2   

#drop two or more columns by using index
df=pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)
df2

df=pd.DataFrame(technologies)
#drop two or more columns
liscol=["Courses","Fees"]
df2=df.drop(liscol,axis=1)
df2   

df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df


#######################################################################

#when we are acccessing the columns by using index then iloc is used
#when we are acccessing the columns by using names then loc is used

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

df=pd.DataFrame(technologies,index=row_labels)
#df.iloc[startrow:endrow,startcol:endcol]
df2=df.iloc[:,0:2]
df2
# it is just operating as a slicing operator
df2=df.iloc[0:2,0:]
df2


#slicing of specific rows and columns using the attributes
df3=df.iloc[1:2,1:3]
df3
df2=df.iloc[2]
df2

df2=df.iloc[[2,3,4]]
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]#select first 3 rows
df2=df.iloc[-1:]#select last 1 row
df2=df.iloc[-3:]#select last 3 rows
df2=df.iloc[::2]#select the alternate rows
