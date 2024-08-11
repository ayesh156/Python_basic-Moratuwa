# The return Statement

# A return statement in a Python function can serve either terminate the function immediately and pass the control of execution back to the caller OR pass any required data back to the function caller.

# In the first situation we just include the return statement but whenever we are returning a specific value/s from the function we need to mention that together with the return statement. And these returned values can be captured by another function or a variable as the program prefers.

# A Python function can return any type of object. And Python allows returning multiple values, separated by commas. There they are actually returned as a tuple.

def totalPrice(qty, price):
    """
    This function return a single value; The total price
    """
    return qty*price

def getItemDetails():
    """
    getItemDetails function return three values: a Tuple of (stock, name, price). but you can receive them as three separate result as well.
    """
    return 15,"Bread",80.00

def showItemDetails(qty,name,price,total):
    """
    showItemDetails function returns nothing: It didplays the details in screen. So the return statement is optional
    """
    print("Qty: {} Item: {} Unit Price: {} Total Price: {}".format(qty,name,price,total))

# Receiving returning result as a Tuple
# details = getItemDetails()
# print(details)

# Receiving returning result as separaet results
stock,itemName,price = getItemDetails()

qty = 10

total = totalPrice(qty,price)

showItemDetails(qty,itemName,price,total)
