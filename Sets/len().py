# Set Operations

# Finding length using len() function

# The cardinality of a set is the number of elements in the set, which can be obtained with built-in function len()

# len() function Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

set1 = set()

# Adding element and tuple to the set

set1.add(8)
set1.add(9)
set1.add((6,7))

print("The length of the set is:", len(set1))