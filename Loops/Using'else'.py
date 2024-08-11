# Using ‘else’ with Loops

# Python allows to use an ‘else’ clause with loops:

# For

# If the ‘else’ clause is used with a for loop, the ‘else’ clause is executed when the loop has iterating the sequence given.

# Assuming loop is not exiting with a break.

# Look at the example code. In this example with an else clause for loop will be executed until it finds the number 5. If it finds number 5 it will exit the loop with a break and after printing number found. If it does not find number 5 it will complete the loop and then go to the else clause and say that the number is not found.

numbers = [3, 2, 6, 8, 2, 9]
for number in numbers:
    print("Looking at :",number)
    if (number == 5):
        print("Found number")
        break
else:
    print("Number not found")

print(" ")

# While

# If the ‘else’ clause is used with a while loop, the ‘else’ clause is executed when the loop condition becomes false.
num = 4
while (num > 5):
    print("Number :",num)
    num -= 1

else:
    print("Incorrect number")