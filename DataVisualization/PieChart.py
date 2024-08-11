# Let us plot a pie chart to inspect the stock percentage bt size. To do that we need the total number of t shirts by size. we can use groupby method available in pandas library to generate this data.

# Lets plot the data we obtained in the above step. Note the first column of a group by method output is an index.
# We are using the pyplot libray to plot pie chart.

# Below we create the above dataset using random function. Let us generate a dataframe for 1000 randomly generate t-shirt information.

import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import string
from scipy import rand
import seaborn as sns

print("matplotlib: {}".format(matplotlib.__version__))

sizes = ["S", "M", "L", "XL", "XXL"]
colors = ["black", "red", "white", "blue"]

# Below we create functions to generate a probable value for each column attribute randomly
def generate_random_id():
    return str(random.randrange(100, 999))+random.choice(string.ascii_uppercase)

def generate_random_size():
    return random.choices(sizes, weights = [0.15, 0.32, 0.28, 0.20, 0.05])[0]

def generate_random_color():
    return random.choice(colors)

def generate_random_price():
    return round(random.uniform(0, 10000),2)

def generate_random_stock():
    return random.randrange(12, 2345)

stock_no_of_tshirts = 1000
data = []
for i in range(stock_no_of_tshirts):
    row = []
    row.append(generate_random_id())
    row.append(generate_random_size())
    row.append(generate_random_color())
    row.append(generate_random_price())
    row.append(generate_random_stock())
    data.append(row)
df = pd.DataFrame(data, columns = ['id', 'size', 'color', 'price', 'stock'])
# print(df)

stock_by_size = df.groupby(['size']).sum()
print(stock_by_size)

plt.pie(stock_by_size['stock'], labels = stock_by_size.index)
plt.title("t-shirt stock")
plt.show()
