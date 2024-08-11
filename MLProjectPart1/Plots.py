# Violin Plots

# Sometimes, the summary statistics such as mean, standard deviation and median are not enough to understand a dataset. Are the values clustered around the median? Are they spread out normally or skewed to one side? A violin plot can help you to answer these questions. This can show you peaks of the data and visualizes the distribution of the dataset.

# Let’s focus on the top right violin plot that shows the distributions of the attribute “petal length”. We can observe that for Iris Setosa, the petal length is distributed between 1 cm and 2 cm with a larger proportion of the flowers having a measurement near the median value. The other two types of Iris have a flatter and longer distributions of petal length with Iris Virginica having the longest distribution with a long thin tail.

# Correlation Heatmap

# Correlation between two attributes tells you about the interdependency between the two attributes. A correlation heatmap shows a 2D visualization of such interdependencies between each pair of attributes. Whether two attributes are highly correlated or not is reflected by the colors of the heatmap. The following code block can be used to plot the correlation heatmap for our dataset.

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
dataset = pd.read_csv(url,names = col_name)

# Violin Plot
sns.violinplot(y='class', x='sepal-length', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='sepal-width', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='petal-length', data=dataset, inner='quartile')
plt.show()
sns.violinplot(y='class', x='petal-width', data=dataset, inner='quartile')
plt.show()

# Pair Plot
sns.pairplot(dataset, hue='class', markers='+')
plt.show()