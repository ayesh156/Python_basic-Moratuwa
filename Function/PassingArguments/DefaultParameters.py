# Default Parameters

# In Functions defined with default parameters, if no argument is passed during the function call, a predefined default parameter is passed as the value for the function. Such parameters are specified in Python function definition in the <name>=<value>, format. This <value> becomes a default value for that parameter.
# when any arguments are left out, the function assumes its default value.

def greet(name, msg="How are you?"):
    print(name + ", " + msg)

greet("Ayesh")
greet("Ayesh", "Good Evening")
greet("Good Evening")


