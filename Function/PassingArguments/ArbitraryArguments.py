# Arbitrary Arguments

# In some function definitions, you will not know the exact number of arguments that need to be passed to the function during its call. In such situations you can use the *args syntax with the function definition.

def add(*args):
    total = (sum(args))
    print("The sum :",total)

def greet(msg, *names):
    for name in names:
        print(msg+", "+name)

#Calling add() function
add(1, 4, 5)

#Calling greet() function
greet("Hello", "Ayesh", "Chathura", "Lucy")