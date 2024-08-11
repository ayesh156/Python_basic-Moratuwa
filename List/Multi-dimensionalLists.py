#  Multi-dimensional Lists

# Up to now, we only looked at one-dimensional lists where a list holds values within square brackets. Python allows the creation of multi-dimensional lists as well.

# If you are unfamiliar with the concept of a matrix, consider it as a simple structure where values are stored in multiple rows and columns. A value in a matrix is denoted by amn where m is the row number and n is the column number

# Using 2-dimensional lists is an easy approach to represent matrices in Python. The following is a 2-dimensional list that stores the matrix

data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

# There are three lists inside another list. Each internal list holds the values of a row in the matrix. For example, the first internal list contains the values [1,1,1] which is the first row in the matrix.

# Accessing the values in a 2-dimensional list is similar to accessing values in a matrix. Suppose we want to access the value in the center square (a22). In the 2-dimensional list data, it is in the internal list at index 1 and inside that internal list, it is at index 1 again. The following code clearly illustrates how to access values in a 2-dimensional list.

data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(data[1][1])

# Other list operations such as update, append, and delete also work in a similar manner. See the example below.

data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
data[1][1] = 25
print(data)

data[1].append(2)
print(data)