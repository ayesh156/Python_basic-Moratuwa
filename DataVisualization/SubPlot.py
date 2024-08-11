#Below we create the above dataset using random function. Let us generate a dataframe for 1000 randomly generate t-shirt information.
import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import string
import seaborn as sns

print("matplotlib: {}",format(matplotlib.__version__))

sizes = ["S", "M", "L", "XL", "XXL"]
colors = ["black", "red", "white", "blue"]

#Below we create functions to generate a probable value for each column attribute randomly.
def generate_random_id():
    return str(random.randrange(100, 999))+random.choice(string.ascii_uppercase)

def generate_random_size():
    return random.choices(sizes, weights = [0.15, 0.32, 0.28, 0.20, 0.05])[0]

def generate_random_color():
    return random.choice(colors)

def generate_random_price():
    return round(random.uniform(0, 10000), 2)

def generate_random_stock():
    return random.randrange(12, 2345)

total_no_of_tshirts = 1000
data = []
for i in range(total_no_of_tshirts):
    row = []
    row.append(generate_random_id())
    row.append(generate_random_size())
    row.append(generate_random_color())
    row.append(generate_random_price())
    row.append(generate_random_stock())
    data.append(row)
df = pd.DataFrame(data, columns = ['id', 'size', 'color', 'price', 'stock'])
#print(df)

stock_by_size = df.groupby(['size']).sum()

dark_stock = [20, 34, 30, 35, 27]
light_stock = [25, 32, 34, 20, 25]

x = np.arange(len(sizes))
width = 0.35

fig, ax = plt.subplots()

#price data 
dark_price = np.random.normal(75, 6, 100)
light_price = np.random.normal(56, 12, 100)
data = list([dark_price, light_price])

#build a box plot
ax.boxplot(data)

# title and axis labels
ax.set_title('box plot: price distribution by color density')
ax.set_xlabel('color')
ax.set_ylabel('price distribution')
xticklabels = ['dark', 'light']
ax.set_xticklabels(xticklabels)

plt.show()