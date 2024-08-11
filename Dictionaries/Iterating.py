# Iterating through a Dictionary

# 1. Using a for loop

test_dict = {"a": 1, "b" : 2, "c" : 3}

# Printing dictionary

print("Original dictionary is : " + str(test_dict))

# Using in operator to
# Get key and value
print("The Key-value are: ")
for i in test_dict:
    print(i, test_dict[i])

# 2. Using enumerate()
# Using in operator to
# Get key and value
print("The Key-value are: ")
for i in enumerate(test_dict.items()):
    print(i)

# 3. Using class method items()
# using dict.items() to
# get key and value
print("The Key-value are: ")
for key, value in test_dict.items():
    print(key, value)

# 4. Using list comprehension
# Using list comprehension to
# Get key and value
print("The key-value are: ")
print([(k, test_dict[k]) for k in test_dict])





