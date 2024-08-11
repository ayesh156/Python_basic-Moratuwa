# Tuples

# Structure of a Tuple

# Tuples contain comma-separated values between round brackets/parentheses. The only difference from lists is that the square brackets in lists are replaced by parentheses.

# The parentheses are not mandatory when creating a tuple. Similar to lists, the values within a tuple need not be of the same data type.

# Creating a Tuple

tuple_1 = ('a', 'b', 20, 4.1)
print(tuple_1)

tuple_2 = 'a', 'b', 20, 4.1 # no parentheses
print(tuple_2)
print(type(tuple_2))

# The variable ‘tuple_1’ contains a tuple with 4 elements. It is important to note that the first two elements ‘a’ and ‘b’ are strings, 20 is an integer and 4.1 is a floating-point number, which are all different data types.

# The data type of a variable can be checked using the type function. If we call type(tuple_1), it outputs ‘tuple’ as the data type.

# In the previous section (1.1) we mentioned that it is not mandatory to have the parentheses when creating tuples. The variable named ‘tuple_2’ contains the same set of elements as ‘tuple_1’ but without the parentheses. If we print ‘tuple_2’, you can see that the system has added the parentheses by itself. When we check the data type of ‘tuple_2’, it is indeed a tuple.

# A tuple with a single element is a special case.

tuple_3 = ('a')
print(type(tuple_3))

tuple_4 = ('a',) # equivalently typle_4 = 'a',
print(type(tuple_4))

# The variable ‘tuple_3’ contains one element which is string ‘a’ inside parentheses. If we check the data type, it turns out to be a string and not a tuple. To create a tuple with a single element, a comma should be included after the element as shown above. If you check the data type of the variable ‘tuple_4’, it is a tuple and not a string. 
