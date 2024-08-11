from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5])
y = np.array([0,1,4,9,16,25])

y2 = y * 2
y3 = y ^ 3

plt.plot(x, y, marker='o', label='y')
plt.plot(x, y2, marker='o', label='y2')
plt.plot(x, y3, marker='o', label='y3')
plt.title('y vs x graph')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()
plt.show()
