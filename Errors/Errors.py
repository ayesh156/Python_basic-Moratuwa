# Syntax Errors

# Refer to the example below. We are trying to print the string ‘Hello World!’ to the console. 
# So, what will happen if we run this code? It will generates a ‘Syntax Error’. We were trying to print a string value and Python was expecting single or double quotation marks. But we mistakenly had one quotation symbol missing at the end of line. Because of that, Python is complaining about a ‘Syntax Error’.

print('hello world)

## Runtime Errors

# Runtime errors occur whenever syntactically correct Python code results in errors at the run-time. There will be an error message telling us what went wrong. 
# It is important to know that whenever a runtime error occurs and it is not handled properly, your Python program will terminate after that point of error. Meaning, the program will not continue to execute and you will not be able to get the expected task done. 
# There are many types of runtime errors in Python.

# NameError

# A ‘NameError’ occurs when you try to reference a variable that has not been defined in the code. In the example you see a variable named ‘number’ with value 10. Then we try to print the value of a variable named ‘num’. Therefore Python is complaining about a NameError and says ‘name ‘num’ is not defined’.

number = 10
print(num)

# IndexError

# This error happens when we try to access a value from a sequence, but the referenced index is out of range. In this example, my_list only has three items, the index is ranging from 0 to 2. But we are trying to access the item at index 10, which is not available. That is why Python is raising an Index Error.

name_list = [1, 2, 3]
print(name_list[10])

# Type Error

# A Type Error occurs when we try to perform an operation on variables of objects of inappropriate type. In this case we are causing a type mismatch. In the example we are trying to perform the ‘+’ operator on a string and an integer. Therefore Python is complaining that it can only concatenate (means to join) a string to string but not to any other data type (in this case an integer). 

str_name = 'colin' + 1
print(str_name)

# Value Error

# A Value Error occurs when a built-in operation or function receives an argument that has the right type but an invalid value. In this case we are trying to print the value of an integer but passing the string value ‘hello’ to the function ‘int’ which is invalid. That is why Python is complaining about a Value Error.

print(int('hello'))

# Import Error / ModuleNotFound Error

# In this example code we are trying to import a module named ‘new_module’ which does not exist. Therefore Python is raising a Module Not Found error. Similar error could occur if you try to import something that does not exist from an existing module.

import new_module