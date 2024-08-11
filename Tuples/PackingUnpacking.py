# Tuple Packing and Unpacking

# Tuple packing is nothing but assigning values into a tuple. In the following example, we are assigning the values ‘car’, ‘pen’ and ‘ice’ into a tuple. This is called tuple packing.

my_tuple = ('car', 'pen', 'ice')

# Tuple unpacking is extracting the content of a tuple into variables. Consider the following example.

a, b, c = my_tuple
print(b)

# We have three variables ‘a’, ‘b’ and ‘c’ on the left-hand side of the equal sign and the tuple ‘my_tuple’ on the right-hand side. The tuple on the right-hand side contains three values ‘car’, ‘pen’ and ‘ice’. The first line of code assigns the content of the tuple to the variables on the left-hand side. Hence the string ‘car’ will be assigned to variable ‘a’, the string ‘pen’ will be assigned to variable ‘b’ and the string ‘ice’ will be assigned to the variable ‘c’. To confirm let us print the variable ‘b’. It outputs the string ‘pen’ as expected.

# One condition when using tuple unpacking is the number of variables on the left-hand side should be equal to the number of elements in the tuple. In the previous example, ‘my_tuple’ contains three elements. Hence, we have three variables on the left-hand side.

# Exercise
# Run the following code and analyze the output.

my_tuple2 = ('car', 'pen', 'ice')
a, b = my_tuple2
print(b)