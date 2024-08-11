# The following example code shows how you can draw a graph using the Matplotlib libraray. If you run the code it will show the plot. Try to see if you can add a few more data points to the graph by changing the code where it is taking the data points to plot.

# import the matplot lib library
import matplotlib.pyplot as plt

# line 1 points
x1 = [10, 20, 30, 40]
y1 = [20, 40, 10, 10]

# line 2 points
x2 = [10, 20, 30, 40]
y2 = [40, 10, 30, 30]

# Set the x axis label of the current axis:
plt.xlabel('x-axis')

# Set the y-axis label of the current axis:
plt.ylabel('y-axis')

# Plot line and/or markers to the Axes.
plt.plot(x1, y1, color= 'blue', linewidth= 3, label= 'line-dotted', linestyle= 'dotted')
plt.plot(x2, y2, color= 'red', linewidth= 5, label= 'line-dashed', linestyle= 'dashed')

# Set a title
plt.title('Plot with two or more lines with different styles')

# Set to show the legends
plt.legend()

# function to show the plot
plt.show()