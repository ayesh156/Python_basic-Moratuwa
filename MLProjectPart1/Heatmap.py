# Correlation Heatmap

# In the first line we specify the size of the figure, in inches. In this case the width is 7 inches and the height is 5 inches. Then we call the heatmap function of Seaborn, to which we pass the correlation matrix of the attributes of the dataset. The calculation of the correlation matrix is achieved by calling the corr() function on the dataset. The cmap variable sets the type of color map we would like to see on the heatmap. Here we have specified cmap=’cubehelix_r’. Have a look at the documentation of the Seaborn library to find out the other kinds of color maps that are available for producing a colorful correlation heatmap.

# IMPORTING LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt
# % matplotlib inline

# LOAD THE DATA
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
col_name = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url, names = col_name)

# Correlation Heatmap
plt.figure(figsize=(7,5))
sns.heatmap(dataset.corr(), annot=True, cmap='jet')


plt.show()