# Passing Arguments

# Most of the functions you will be defining needs data being passed into it, in the form of parameters. In Python there are varied ways of function invocation.

# Positional Arguments

# Positional Arguments is the most common and straightforward method of passing arguments to function. During the definition of the function you also specify the list of parameters that the function accepts, within parenthesis as below.

# You are not allowed to leave any out, or specify extra ones when calling the function, as shown in the following.

# Function definition
def calc(qty, item, price):
    print("The" +item+" cost/s",(qty*price),"rupees")

# Function call
calc(2, 'Apple', 20)


