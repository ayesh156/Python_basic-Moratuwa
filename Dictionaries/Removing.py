# Removing an element

# 1. Using the del keyword.

# The keys in a Python dictionary can be deleted using the del keyword.
# There are 2 ways in which the del keyword can be used.

# We can delete either specific entries in the dictionary with the use of selected keys.
# We can delete the entire dictionary.(Once we delete a dictionary, it is no longer available in a program.)

# 2. Using the built-in function pop().

# An entry in a dictionary can be removed using the built-in function pop() and specifying the key as an argument. The pop() method will return the value from the dictionary while deleting the full entry.

# 3. Using the built-in function popitem().

# The popitem() method will return an arbitrary element as a tuple (that is, a (key, value) pair) from the dictionary while deleting the full entry.

# Removing all elements

# Using the built-in function clear() method will delete all the items from a dictionary at once. Unlike the deletion of a dictionary that we can do with del keyword, a cleared dictionary is still available in a program.

test_dict = {'Alex': 'Phone', 'Jane': 'Laptop', 'Karl': 'Laptop', 'Anita': 'Tablet'}

# del keyword
del test_dict['Alex']
print(test_dict)

# built-in pop() function
element = test_dict.pop('Karl')
print(test_dict,f'\nThe element which was poped - {element}')

# built-in popitem() function
item = test_dict.popitem()
print(test_dict,f'\nThe item which was poped - {item}')

# built_in clear() function
test_dict.clear()
print(test_dict)

# deletion of the dictionary
del test_dict
print(test_dict) # This will raise an error