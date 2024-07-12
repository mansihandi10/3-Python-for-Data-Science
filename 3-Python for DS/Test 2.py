# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:21:13 2024

@author: Hp
"""
#Write a Python function that takes two lists and returns True if they have at least one common member.

def com_num(lst1, lst2):
    # Convert the first list to a set
    set1 = set(list1)
    
    # Check each element in the second list
    for item in lst2:
        if item in set1:
            return True
    
    # No common elements found
    return False

# Example usage:
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 3]
print(com_num(list1, list2))  # Output: True

lst3 = [1, 2, 3]
lst4 = [4, 5, 6]
print(com_num(list3, list4))  # Output: 
    
    
#####################################################################

#Use list comprehension to construct a new list but add 6 to each item.

original_list = [1, 2, 3, 4, 5]
new_list = [item + 6 for item in original_list]

print(new_list)  # Output: [7, 8, 9, 10, 11]

#########################################################################

#Write a Python program to reverse a string. 

name="Mansi"

rev_str=name[::-1]
print(rev_str)
############################################################
#Open the file data.txt using file operations. 
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

###########################################################################

#Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data 
import numpy as np
import pandas as pd
arr = np.array([11, 22, 33, 44, 55])

print(arr[0])
print(arr[4])



#############################################################################

#Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4 


import pandas as pd
import numpy as np

arr=np.array([11,22,33,44,55])

print(arr[1:4])

##########################################################################
"""Write a Python program to filter a list of integers using Lambda.  
Original list of integers: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Even numbers from the said list: 
[2, 4, 6, 8, 10] 
Odd numbers from the said list: [1, 3, 5, 7, 9
"""

# Original list of integers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering even numbers using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))

# Filtering odd numbers using lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))

# Output
print("Original list of integers:")
print(original_list)
print("Even numbers from the said list:")
print(even_numbers)
print("Odd numbers from the said list:")
print(odd_numbers)


#############################################

"""Write a Pandas program to create the specified columns and rows from a given data frame. 
name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh'] 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19] 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1] 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
"""

import pandas as pd
import numpy as np

# Data
'data = {
    'name': ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'Venkat', 'Ajay', 'Dhanesh'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Creating DataFrame
df = pd.DataFrame(data, index=labels)

# Display the DataFrame
print(df)

#Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.


# Sample dictionary
original_dict = {
    'item1': 1500,
    'item2': 2500,
    'item3': 3000,
    'item4': 1900,
    'item5': 2200

}

# Dictionary comprehension to filter out key:value pairs where values are greater than 2000
filtered_dict = {key: value for key, value in original_dict.items() if value > 2000}

# Display the new dictionary
print(filtered_dict)
