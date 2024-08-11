# Pandas

# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name Pandas has a reference to both Panel Data, and Python Data Analysis and was created by Wes McKinney in 2008.
# https://github.com/pandas-dev/pandas

# Import Pandas

# Install pandas: 
# conda install pandas
# pip install pandas

# Import: 

import pandas as pd

# Check Version:  

print(pd.__version__)

# Data Structures in Pandas

# Series — 1D
# DataFrame — 2D
# Panel — 3D

# Series

# The Series is the object of the pandas library designed to represent one-dimensional data structures.
# Similar to an array but with some additional features. 

# A series consists of two components.

# One-dimensional data (Values)
# Index

# Working with Series

import pandas as pd
a_dict = {'1st': 1, '2nd': 3, '3rd': 5, '4th': 7, '5th': 9}
ser = pd.Series(a_dict)
print(ser)

print('Range access:')
print(ser[0:3])

print('Access: Index number')
print(ser[1])

print('Access: Index label')
print(ser['2nd'])

# DataFrame

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as pd
data = {'catogeries': [420, 380, 390], 'duration': [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

# Reading From CSV File

# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contain plain text and are a well know format that can be read by everyone including Pandas.
# In our examples, we will be using a CSV file called student.csv

import pandas as pd
df = pd.read_csv('student.csv')

print(df)

# Analyzing DataFrames

# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.

import pandas as pd
df = pd.read_csv('student.csv')

print(df.head(5))

# Pandas - Cleaning Data

# Data cleaning means fixing bad data in your data set.
# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Handling Empty Cells

# Empty cells can potentially give you a wrong result when you analyse data.

# 1. Remove Rows with empty cells: dropna()

# By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:

import pandas as pd
df = pd.read_csv('student.csv')

newdf = df.dropna()
print(newdf.to_string())

# 2. Replace Empty Values: fillna()

# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.

import pandas as pd
df = pd.read_csv('student.csv')

newdf = df.fillna('male')
print(newdf.to_string())

# Fixing Data

# Suppose we have a dataFrame mentioned in slide 10.
# Let’s say that the duration cannot be more than 70.
# Then we can fix it by setting any duration value higher than 70 to 70.

import pandas as pd
df = pd.read_csv('student.csv')

for x in df.index:
    if df.loc[x, 'mark'] > 70:
        df.loc[x, 'mark'] = 70

print(df.to_string())

# Handle Duplicates

# Duplicate rows are rows that have been registered more than one time.
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:

import pandas as pd
df = pd.read_csv('student.csv')

print(df.duplicated())

# To remove duplicates, use the drop_duplicates() method.

print(df.drop_duplicates())

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['a']) 