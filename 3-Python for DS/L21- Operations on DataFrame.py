# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:31:29 2024

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

#shuffling of data

df1=df.sample(frac=1)#frac=1 meang 100 per shuffle of data will be there if frac =0.5 the 50 percent data is going to shuffle
df1

#to create new index starting from zero 
df1=df.sample(frac=1).reset_index()#frac=1 meang 100 per shuffle of data will be there if frac =0.5 the 50 percent data is going to shuffle
df1

#drop shufflw index
df1=df.sample(frac=1).reset_index(drop=True)#frac=1 meang 100 per shuffle of data will be there if frac =0.5 the 50 percent data is going to shuffle
df1


import pandas as pd
import  numpy as np
technologies={
    "Courses":["Spark","Pandas","Python","Numpy"],
    "Fees":[20000,30000,40000,80000],
    "Duration":["30 Days","30 Days","30 Days","30 Days",]

    }
row_labels1=['r0','r1','r2','r3']
df1=pd.DataFrame(technologies,index=row_labels1)
df

technologies={
    "Courses":["Spark","Java","Python","Go"],
     "Fees":[20000,30000,40000,80000]
    }
row_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies,index=row_labels2)
df


#pandas join

df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
df3

#inner join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='')
df3

#another meging method is also there

df3=pd.merge(df1,df2)
df3
df3


#concate thye multiple data frames using the pandas.concate()
import pandas as pd

df=pd.DataFrame({'Courses':[""]})



























