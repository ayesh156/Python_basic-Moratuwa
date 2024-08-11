# Defining a Dictionary

# 1. Using Curly Brackets to initialize a dictionary.
# To create an empty dictionary, we simply use the curly braces { } without any data elements inside.

# {} symbol to initialize dictionary
emptyDict = {}

# print dictionary
print(emptyDict)

# print length of dictionary
print("Length: ",len(emptyDict))

# print type
print(type(emptyDict))

# example
test_dictionary = {1: 'Ayesh', 2: 'Chathuranga', 3: 'Chathura'}

print(test_dictionary)

thisDict = {
    "brand": "Nissan",
    "model": "D21",
    "year": 1989
}

print(thisDict)

# 2. Use of dict() built-in function.

# A common and useful way of creating dictionaries is to use a sequence (say, a list) of pair-type tuples where the first value in the pair is the key and pass it to the Python built-in function dict().

# initialize dictionary
emptyDict2 = dict()

# print dictionary
print(emptyDict2)

# print length of dictionary
print("Length: ",len(emptyDict2))

# print type
print(type(emptyDict2))

#example
test_dictionary2 = dict([('offroad', 'Hilux'), ('Cargo', 'Hiace'), ('Luxury', 'Crown')])

print(test_dictionary2)