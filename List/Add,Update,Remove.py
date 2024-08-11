# Appending Values to a List

# To append 60 to this list, which means adding 60 to the end of this list, the append() method can be used. The following code demonstrates how the append() method is used.

values = [15, 20, 96, 32, 17]
values.append(60)
print(values)

# The output shows that 60 has been appended successfully.

# Updating a Value in a List

# Suppose we need to update the value at index 2, which is 96, to 60. It can be achieved in the following manner.

values = [15, 20, 96, 32, 17]
values[2] = 60
print(values)

# To update the value at a specific index, we write the name of the list followed by the index in square brackets on the left-hand side of the equal notation and the new value on the right-hand side of the equal notation (e.g., values[2] = 60).

# Deleting a Value from a List

# Suppose we need to delete the value at index 1. It can be achieved using the remove() method as shown below.

values = [15, 20, 96, 32, 17]
values.remove(20)
print(values)

# The output does not contain 20 which was the value at index 1. One drawback in using the remove() method is that the value at the specific index should be known. For example, in the above example, the remove() method cannot be used if we do not know that 20 is the value at index 1. In scenarios where the value at a specific index is not known, an alternative approach is to use the del (delete) keyword. See the following example.

values = [15, 20, 96, 32, 17]
del values[1]
print(values)

# The del keyword does not need the value at an index to be known.

# Practice Exercise 1

# What will be the output when the following code is executed?

list = ['ph', 'ch', 1997, 2000, 2000, 2009]
list[2] = 2001
list.remove(2000)
list.append(2015)
print(list[2:])