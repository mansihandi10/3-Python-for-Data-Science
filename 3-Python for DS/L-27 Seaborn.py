# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:19:47 2024

@author: Hp
"""
#seaborn

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

cars=pd.read_csv("cars.csv")
cars
""" HP        MPG  VOL          SP         WT
0    49  53.700681   89  104.185353  28.762059
1    55  50.013401   92  105.461264  30.466833
2    55  50.013401   92  105.461264  30.193597
3    70  45.696322   92  113.461264  30.632114
4    53  50.504232   92  104.461264  29.889149
..  ...        ...  ...         ...        ...
76  322  36.900000   50  169.598513  16.132947
77  238  19.197888  115  150.576579  37.923113
78  263  34.000000   50  151.598513  15.769625
79  295  19.833733  119  167.944460  39.423099
80  236  12.101263  107  139.840817  34.948615

[81 rows x 5 columns]"""
cars.head()
"""HP        MPG  VOL          SP         WT
0  49  53.700681   89  104.185353  28.762059
1  55  50.013401   92  105.461264  30.466833
2  55  50.013401   92  105.461264  30.193597
3  70  45.696322   92  113.461264  30.632114
4  53  50.504232   92  104.461264  29.889149"""
cars.columns
#Index(['HP', 'MPG', 'VOL', 'SP', 'WT'], dtype='object')

sns.relplot(x="HP",y="MPG",data=cars)
sns.relplot(x="HP",y="MPG",data=cars,kind="line")

#boxplaot
sns.catplot(x="HP",y="MPG",data=cars,kind="box")

#histogram

sns.distplot(cars.HP)
#EDA

cars.describe()
"""
               HP        MPG         VOL          SP         WT
count   81.000000  81.000000   81.000000   81.000000  81.000000
mean   117.469136  34.422076   98.765432  121.540272  32.412577
std     57.113502   9.131445   22.301497   14.181432   7.492813
min     49.000000  12.101263   50.000000   99.564907  15.712859
25%     84.000000  27.856252   89.000000  113.829145  29.591768
50%    100.000000  35.152727  101.000000  118.208698  32.734518
75%    140.000000  39.531633  113.000000  126.404312  37.392524
max    322.000000  53.700681  160.000000  169.598513  52.997752"""

#the data is right skewed 
sns.catplot(x="HP",y="MPG",data=cars,kind="box")

plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.displot(cars.HP)

plt.boxplot(cars.HP)

sns.displot(cars.MPG)

plt.boxplot(cars.MPG)

sns.displot(cars.VOL)
plt.boxplot(cars.VOL)

sns.displot(cars.SP)
plt.boxplot(cars.SP)

sns.displot(cars.WT)
plt.boxplot(cars.WT)


#joinplot
import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars['MPG'])

#countplot

plt.figure(1,figsize=(16,10))
sns.countplot(cars["HP"])

# To find the smallest number

a = int(input("Enter Number: "))
b = int(input("Enter Number: "))
c = int(input("Enter Number: "))

if a < b and a < c:
    print(a, "is smaller")
elif b < c:
    print(b, "is smaller")
else:
    print(c, "is smaller")
