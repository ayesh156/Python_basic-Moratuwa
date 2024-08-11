#  Tuple Operations

# This section discusses some common tuple operations.

# Length

# To find the size/length of a tuple, the function ‘len’ (stands for length) can be used. See the following example.

print(len((1,2,3)))

# The length of the tuple is 3 as it contains 3 values.

# Concatenation

a = (1,2,3)
b = (4,5,6)
print(a+b)

# Suppose there are two tuples a and b. The contents of tuples a and b can be combined using the plus(+) operator. a+b will output a single tuple with contents from tuples a and b. In the output of the above example, values 1, 2, and 3 are from tuple a, and values 4, 5, and 6 are from tuple b.

# Repetition

# The following code illustrates how repetition works.

print(('Hi',) * 4)

# Note that in the above example, multiplying by 4 does not create 4 separate tuples but a single tuple where the contents of the original tuple are multiplied 4 times.

# Membership

# Membership checks whether a value is available in a tuple. See the following example.

print(3 in (1,2,3))

# The ‘in’ operator is used to check membership. Statement ‘3 in (1,2,3)’ checks whether value 3 is available in the tuple. Since the value is available, it returns True. If the value is not available, it will return False.

# Iteration

# Iteration means going through the tuple one element at a time. 

for x in (1,2,3):
    print(x)

# The first element in the tuple, which is 1 in the example above, will be assigned to the variable x. Then the print(x) statement will be executed. After that, the second value in the tuple, which is 2, will be assigned to the variable x. The print(x) statement will be executed again. This pattern continues until the last element in the tuple.