## Break and Continue statements

# Python allows terminating the iteration of the loop prematurely with the break and continue keywords. 

# Break

# With the break statement, the loop can immediately be terminated in entirety. Once a break statement is met within the loop ,the loop is exited and the program execution is passed to the first statement that appears after the loop body.

# Continue

# With the continue statement, the current loop iteration is immediately terminated.This statement skips the rest of the loop statement and starts the next iteration of the loop to take place.

# In while loops,

# Break
n = 10
while (n > 0):
    n -= 1
    if n == 5:
        break
    print(n)

print(" ")

# Continue
n = 10
while (n > 0):
    n -= 1
    if n == 5:
        continue
    print(n)

print(" ")

# In for loops

# break and continue work the same way with for loops as with while loops. break terminates the loop completely and proceeds to the first statement following the loop, and continue terminates the current iteration and proceeds to the next iteration:

# Break
for i in ['rabbit', 'deer', 'lion', 'giraffe']:
    if 'lion' in i:
        break
    print(i)

print(" ")

# Continue
for i in ['rabbit', 'deer', 'lion', 'giraffe']:
    if 'deer' in i:
        continue
    print(i)
