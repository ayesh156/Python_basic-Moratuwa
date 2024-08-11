# Python Dictionary Operations

# Refer to the examples below on adding and updating elements.
car_dict = {'brand': 'Lamboghini', 'model': 'Miura', 'year': 1973}

#Adding an element
car_dict['type'] = 'sports'
print(car_dict)

#Updating an element
car_dict['type'] = 'exotic'
print(car_dict)

# Note: Both the Subscript Notation and the built-in update() function can be used to add an element or update an existing element of a dictionary.
dictionary = {'string_1': 'I', 'string_2': 'want'}

# Using the subscript notation
# Dictionary_Name[New_Key_Name] = New_Key_Value

# Updating
dictionary['string_2'] = 'need'

# Adding
dictionary['string_3'] = 'some'

# Using the built-in update() function
# Adding
dictionary.update({'string_4': 'water'})
print(dictionary)

# Adding dictionary (string_5 and string_6) to dict
dict1 = {'string_5': 'thirsty', 'string_6': 'quickly'}
dictionary.update(dict1)
print(dictionary)

# Updating by assigning
dictionary.update(string_4= 'juice')
print(dictionary)
