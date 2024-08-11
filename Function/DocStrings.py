# Docstrings

# The Docstrings are supposed to provide detailed documentation for a function. It can be composed of the function’s purpose, its list of arguments, its return values and any other information that the programmer thinks important to mention.

# A docstring is added as the first statement in the body of a Python function. These need to be within quotation marks and the recommended convention to use the triple-quotes (in double quotes) as “”” docstring “”” . These can be on a single line or be multi lined as well. If the docstring fits on a single line both the opening and closing quotes should be on the same line.

# We can also view the docstrings of built-in and user defined functions using the __doc__ attribute.

def calc(qty, price):
    """Returns the product of quantity and price"""
    return qty*price

print(calc.__doc__)

# Docstrings seem to be similar to the commenting. But the difference is that comments are not accessible for viewing during the program execution. And the purpose docstrings serve is different, they are in fact a more useful way of commenting.

print(print.__doc__)

