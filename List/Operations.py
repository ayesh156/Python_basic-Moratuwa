# List Operations

# This section discusses some other common list operations.

# Length

# To find the size/length of a list, the function ‘len’ (stands for length) can be used. See the following example.

print(len([1, 2, 3]))

# The length of this list is 3 as the list contains 3 values.

# Concatenation

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

# Suppose there are two lists a and b. The contents of lists a and b can be combined using the plus(+) operator. a+b will output a single list with contents from lists a and b. In the output of the above example, values 1, 2, and 3 are from list a, and values 4, 5, and 6 are from list b.

# Iteration

# Iteration means going through the list one element at a time.

for x in [1, 2, 3]:
    print(x)

# The first element in the list, which is 1 in the example above, will be assigned to the variable x. Then the print(x) statement will be executed. After that, the second value in the list, which is 2, will be assigned to the variable x. The print(x) statement will be executed again. This pattern continues until the last element in the list.