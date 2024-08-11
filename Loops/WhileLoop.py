## While loop

# The basic syntax of the Python while loop is,

# while <condition>:
#       <statement(s)>

# The line/set of lines to be executed as the loop body is denoted here as <statement(s)> with the imperative indentation, just as in all python control structures.  The <condition> is the loop controlling condition. It has to be declared and assigned an initial value before the start of the while loop. Its value is then modified within the loop body to keep the loop running.

# When the loop strats, the <condition> is evaluated in the form of a Boolean expression, which turns out either to be true or false. The loop body is executed only if the <condition> is true. If it is evaluated to False , the loop will not be executed at all. As mentioned before, the loop controlling variable in the <expr> is modified repeatedly within the loop body and is repeatedly evaluated in each iteration before entering into the loop body.

# This is how it will execute. First we make num to be 5. Then it will check the condition which is true and procced to execute the loop body. At each iteration it will reduce number by 1 and finaly when it becomes 0 it will get out of the loop and complete the code.

num = 5
while (num != 0):
    print("Hello World")
    num = num - 1
