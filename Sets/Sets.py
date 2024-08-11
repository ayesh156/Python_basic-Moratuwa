# Sets

# A set, in mathematics, is defined as a collection of distinct objects. Set is one of 4 built-in data types in Python used to store collections of data. Sets are used to store multiple items in a single variable. A set is a collection that is unordered, iterable, mutable*, unindexed, and duplicate elements are not allowed. The elements in a set are heterogeneous and therefore need not be of the same data type.

# * Note: Set elements are unique and Immutable, but a set is mutable.

# When to use sets?

# ▪When the order of the elements does not matter.
# ▪When you need to have a collection of unique elements.

# Creating sets in python

# A set is created by placing all the items (elements) inside curly braces {}, separated by commas, or by using the built-in set() function.

# Set of integers
my_set = {1,2,3}
print(my_set)

# Set of mixed datatypes
my_set2 = {1.0, "Hello", (1,2,3)}
print(my_set2)

# No duplicates
my_set3 = {1,2,3,4,3,2}
print(my_set3)

# We can make set from a list
my_set4 = set([1,2,3,2])
print(my_set4)

# Set cannot have mutable items
# this will cause an error






y = {('one', 'two'), 'hello', 14}
print(y)