# Insertion, Deletion, and Update

# Let us run the following code.

my_tuple = (15, 20, 96, 32, 17)
my_tuple[0] = 8

# It will output the following error message.

# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     my_tuple[0] = 8
# TypeError: 'tuple' object does not support item assignment

# The reason for this error is because tuples are immutable. It means once a tuple is created, it cannot be modified. Hence, a tuple does not support insert, delete, and update operations. Unlike tuples lists are mutable. We can insert, delete, and update values in a list.