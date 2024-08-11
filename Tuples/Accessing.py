#  Accessing Values in a Tuple
# Accessing values in tuples is similar to lists. Consider the tuple that contains 5 elements 15, 20, 96, 32 and 17.

my_tuple = (15, 20, 96, 32, 17)
print(my_tuple[0])
print(my_tuple[4])

# To create the tuple we code, ‘my_tuple = (15, 20, 96, 32, 17)’. The parentheses are optional. Similar to lists, tuples are also indexed starting from 0.

# Hence, when we call my_tuple[0], it will output the first element in the tuple which is 15. Similarly, if we want to access 17 which is at index 4, we call my_tuple[4]. We get the expected output which is 17.

# Negative Indices

# Negative indices also work similar to lists. We have learnt in course 1 that in negative indexing, the last element is indexed -1 and the values are indexed from right to left.

my_tuple2 = (15, 20, 96, 32, 17)
print(my_tuple[-1])
print(my_tuple[-3])

# When we call my_tuple[-1], we get the last element 17 as the output. Similarly, my_tuple[-3] will return the element at index -3 which is 96.

# Slicing

# Slicing means extracting a part of a sequence. Slicing is the same as what we learnt in the lesson on lists.

my_tuple3 = (15, 20, 96, 32, 17)
print(my_tuple3[0:3])
print(my_tuple3[2:4])

# What will happen when we call my_tuple[0:3]. It will output the values from index 0 to index 2. Remember, if the range is from m to n, the values considered will be from index m to n-1. Therefore, the output will contain 15, 20 and 96. Similarly, if the range is from 2 to 4, the values at indices 2 and 3 will be outputted.

#  Nested Tuples

# Nested tuples are similar to nested lists. Let us create a nested tuple first.

my_tuple4 = ((1, 2), ('a', 'b'))
print(my_tuple4[0][1])
print(my_tuple[1])

# This variable ‘my_tuple’ contains two tuples inside another tuple. The first inner tuple contains the values 1 and 2 while the second inner tuple contains the values ‘a’ and ‘b’. Suppose we want to access the value 2. First, we need to access the inner tuple at index 0 and inside that inner tuple, 2 is located at index 1. Hence, we call my_tuple [0][1] where the 0 points to the inner tuple at index 0 and 1 points to the element at index 1 inside that inner tuple.

# Similarly, if we want to access the inner tuple that contains the values ‘a’ and ‘b’, we know that it is located at index 1. Hence, calling my_tuple[1] will output the entire tuple at index 1 as shown above.