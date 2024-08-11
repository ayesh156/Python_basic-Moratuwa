## Handling Runtime Errors

# As we have discussed before, when a runtime error occurs, the program will stop immediately if the error was not handled properly. Therefore we need to plan carefully to ‘catch’ any possible errors during runtime and handle them. That way we can keep and uninterrupted execution of our program. 

# The try/except Structure

# The try/except structure helps us to handle possible runtime errors. It does not mean that we can prevent the errors. Instead it creates a safe passage for the program in the case of runtime error. 

# We can basically identify two blocks (try and except) in this structure. We can put the so called ‘dangerous code’ into the try block. That means you are anticipating an error in that section of the code. In the case where the error actually occurs, the program jumps to the except block and executes what’s inside that block and moves on with the program.

# Notice that if we did not use this error handling structure, that program will terminate as soon as the error occurs.

# Example
# Below is a simple example of a try/except structure. In this program we are expecting a number as input from the user. Once some input is provided, the program will try to convert that into and integer value. It is actually the risky operation. Because we can not guarantee that the user will provide a number. 

# For example the user can provide a string or just input nothing at all. In such a case, the program will have a problem converting anything other than a number to integer. In normal circumstances, the program will complain about the issue and terminate. But in our example, in such a problematic situation, the program will jump to the except block and assign the value -1 to the variable num_val. So it will prevent ungraceful termination of the program.

num_input = input("Enter a number:")

try:
    num_val = int(num_input)
except:
    num_val = -1

if num_val > 0:
    print("A number was entered!")
else:
    print("Not a number!")