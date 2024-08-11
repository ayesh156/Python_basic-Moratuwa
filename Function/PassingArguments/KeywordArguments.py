# Keyword Arguments

# Another way to call the functions is with Keyword arguments where you can specify the passed arguments in <keyword>=<value> format.The <keyword> is what you have provided as the parameter and the value is the actual parameter value you want to pass to the function.

# The speciality with Keyword arguments use is that you don’t need to worry about the argument order like you did previously. As each argument you pass is specified with the parameter/Keyword name Python can identify the values even though the order is messed up.

# However, here too, the number of arguments should be equal to what is defined in the function.

# The previous function calc() can also be called with keyword arguments as shown below.

def calc(qty, item, price):
    print("The "+item+" cost/s",(qty*price),"rupees")

# Fuction call
calc(qty=5, price=10, item="Oranges")