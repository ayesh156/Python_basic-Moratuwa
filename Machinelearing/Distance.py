# Example code to label data based on distance

# The following code is using a few data points given to it regardging rain and no rain to label a new unknown data point. Play with the code and see if you can understand how it works.

import matplotlib.pyplot as plt

# Training Data Examples for rain and no_rain
rain_temp, rain_humidity = [45, 55, 55], [60, 65, 55]
no_rain_temp, no_rain_humidity = [35, 50, 40], [45, 30, 35]

# Unknown new data point that needs to be labelded for rain or no rain
new_data_temp, new_data_humidity = 40, 50

# Plot the data points for rain / no_rain and unknown new data
plt.scatter(rain_temp, rain_humidity, marker='^')
plt.scatter(no_rain_temp, no_rain_humidity, marker='o')
plt.scatter(new_data_temp, new_data_humidity, marker='x')
plt.legend(['rain', 'no_rain', 'new_data'])
plt.xlabel('temperature')
plt.ylabel('Humidity')
plt.show()

# Simple distance based approach to lable the unknown new data point
rain=0
no_rain=0
sz=len(rain_temp)
for i in range(sz):
    rain+=abs(rain_temp[i]-new_data_temp)
    rain+=abs(rain_humidity[i]-new_data_humidity)
    no_rain+=abs(no_rain_temp[i]-new_data_temp)
    no_rain+=abs(no_rain_humidity[i]-new_data_humidity)
print('Distance to Rain data =', rain)
print('Distance to Not Rain data =', no_rain)

# Print the label of unknown new data point based on the total distance to each group
if rain < no_rain:
    print('It is going to RAIN')
else:
    print('It is NOT going to RAIN')

# In this code the total distance from the unknown new data point to the members of each group is calculated to see how far it is from each group. The rain or no_rain label is asigned to the closest group. The distance is calculated by adding the distance on the x-axis and the y-axis. Not the direct line distance between two points. This is called the Manhatten distance. The direct line distance is called the Euclidean distance as shown in the diagram given below. Try to see if you can change the code to use the Euclidean distance so that you can improve the labeling of the unknown data point. Also note that since we are comparing two distance values to make a decision, we can leave the Euclidean distance in the squared form rather than taking the square root.

# Note when you use Python libraries for building ML models all this will be just an API call!