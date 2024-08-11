# Functions

# In programming, a function is a self-contained block of code that encapsulates a specific task or related group of tasks. They run only when specifically called within the program. The prime advantage of functions is the code re-usability and manageability.

#   Built in Functions in Python

# In previous lessons of this course, you have been introduced to some of the built-in functions provided by Python.  print() for example, takes five arguments, only the first is frequently used, and displays the passed string/object on the screen, unless specified to be written into a file. Function input() lets you insert values to the program.

# In these builtin functions, the code that accomplishes the task is abstracted out from you and you only need to know the function arguments and the values it's returning, whenever you are going to call it.

#   User Defined Functions

# You can define your own functions to manage and reuse the lines of code you may need within the program.

# Function Calls and Definition

# The usual syntax for defining a Python function is as,

# def <function_name>([<parameters>]):
#     <statement(s)>
 
# def is the keyword that we use to inform Python of the new function we re creating. Function name is the identifier, and this should also follow the naming conventions that we learnt in variables tutorial. The component named <parameter/s> is optional. It is there we provide the parameters to be passed to the function, if any are needed. The indented <statement/s> compose the function body defining the functionality. We include the statements we need executed when the function is called , there.

# The syntax for calling a Python function is as,

# <function_name>([<arguments>]):

# <arguments> are the values that are passed into the function when it is called. They correspond to the <parameters> in the particular function definition.

# Even if you define a function that does not need taking any arguments, the parentheses are a must.

def my_function():
    print("Hello from a function")


# Function invocation
my_function()

# Empty Functions

# Sometimes you may need to define a function with an empty body, one that does nothing. This is usually to act as a placeholder until the function is implemented at a later level. Anyhow, when you define empty functions you must use the pass statement.

def empty_func():
    pass

empty_func()