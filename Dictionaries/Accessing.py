# Accessing elements of a dictionary

# Dictionary is quite a useful data structure in programming that is usually used to hash a particular key with value so that they can be retrieved efficiently.

# You can access the items of a dictionary by referring to its key name, inside square brackets.
# There is also a method called get() that will give you the same result.
univ_dict = {
    "University": "University of Moratuwa",
    "Location": "Katubedda",
    "Country": "Sri Lanka"
}

print(univ_dict["University"])
print(univ_dict.get("University"))

# The keys() method will return a list of all the keys in the dictionary.
# The values() method will return a list of all the values in the dictionary.
# The items() method will return each item in a dictionary, as tuples in a list.

univ_dict = {
    "University": "University of Moratuwa",
    "Location": "Katubedda",
    "Country": "Sri Lanka"
}

print(univ_dict.keys(), "\n")
print(univ_dict.values(), "\n")
print(univ_dict.items())