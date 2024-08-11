# Getting started with your python environment

# You can use your favorite python IDE for your machine learning project. However it’s important to note that Google Colab is increasingly popular among ML enthusiasts, mainly because it provides a hassle free rapid start. It is a Jupyter notebook-like programming environment with a large number of standard libraries preinstalled. It also allows you to run your code either on your local machine or in the cloud, allowing you to leverage GPU based computation for better performance for some algorithms.

# https://colab.research.google.com

# Once you open your editor, you can start your python script with the necessary packages imported.

import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt
# % matplotlib inline

# Let’s look at some of the above libraries in a bit more detail

# NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines etc. It is one of the fundamental scientific libraries.
# Pandas is a fast, powerful, flexible and easy to use library for data analysis and manipulation.
# Matplotlib is a comprehensive library for creating static, animated and interactive visualizations.
# Seaborn is a data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
# The command %matplotlib inline allows the plots to be visualized directly inside the python notebook you are coding on.

# Apart from the above, we will also be using Scikit-learn, which is a comprehensive machine learning library that includes implementations of several machine learning algorithms and support functions for training and evaluating machine learning models.

# Exploring the data

# Let’s get our hands on the dataset and see what’s in there! 

# Load the data

# The following code can be used to download the data and load it into a data structure called a DataFrame defined in

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
col_name = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url,names = col_name)

# Pandas. provides a function called head() to print the top five rows of the dataset.print(dataset.shape)
print('Dataset Size')
print(dataset.shape)

# Looking at the top five rows of the dataset

# Pandas provides a function called head() to print the top five rows of the dataset.
print('First Five Rows of the Dataset')
print(dataset.head())

# Look at some summary statistics of the dataset

# Pandas provides a function called describe() to compute and print out summary statistics for each class, such as the number of data points, mean value, standard deviation, minimum value, maximum value and the quartiles.

print('Summary Statistics of the Dataset')
print(dataset.describe())

# See what data types we are dealing with, and the memory usage of the dataset

# Pandas provides a function called info() that prints out the data type of each column andthe memory usage.

print('Data Types and Memmory Usage')
print(dataset.info())

# The number of classes and the number of examples

# Pandas provides a function called value_counts() to show us the number of examples in each class.

# The value_counts() functions should be called on the column that contains the class labels. That is obtained by dataset[‘class’], on which the value_counts() function should be called.

print('classes and the number of examples')
print(dataset['class'].value_counts())