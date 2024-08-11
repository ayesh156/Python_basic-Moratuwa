# Loops and Iterations

# Iteration is the repeated execution of the same block of code. 

# Why do we need Loops and Iterations ?

# Why do we repeat? Let’s say that we want to enter marks for a student and check to see if the student has passed the exam by getting more than 50 marks. We would write one line of code for one student. Now let’s say thea we have 5 students and we want to do the same. One way of doing this is to copy the code written for one student 5 times. 

# Is this the best way of doing this? If we had a way of writing the code once yet repeat it 5 times. it would be easier to write and if necessary, change languages allow us a way to repeatedly execute code multiple times.

# We already know how to write code that goes in a sequence. We also we know how to write code to check some condition and decide which way to go using if-else and switch- case in python.

# Considering the nature of iterations, these can be categorized as,

# Definite iteration, in which the number of repetitions is specified explicitly in advance
# Indefinite iteration, in which the code block executes until some condition is met
# In Python, indefinite iteration is performed with a while loop, and definite iteration is implemented with for loops.

## The for Loop

# In the for loop the block of code is repeated or iterated a specific number of times. The format of the code or the syntax of the code is to have the for Keyword and tell that for each iterating variable in the sequence needs to loop through the code.

# for iterating_var in sequence:
#     statements(s)

# "For" and "in" are the two keywords. The iterating variable and the sequence are variables that we define. The sequence can be a list of numbers where each time the iterating variable will be taking an item starting from the first one until it reaches the end of the list. And we also have a colon. Don’t forget the colon if you forget you will get a syntax error 

# The block of statements repeated is called the loop body. The loop body needs to be indented to the right so that the computer understands the block of code belongs to this loop. 

# Let us look at an example in python. Play around with the code to see if you can add one more iteration to the given code example.

for counter in [1, 2, 3, 4, 5]:
    print("This is a loop counter = ", counter)
print(" ")

# Range Function

# It may be not practical for us to type the sequence of items that we want the iterating variable to take. So we have the range function to create the sequence of numbers we want. 

# One way of indicating range function is to input when to stop the sequence. So if we input 10 the sequence will have 10 numbers from 0 to 9. The sequence ends at 9 because 0 is counted as an item in the sequence.

# range(stop)
# example:
for i in range(10):
    print(i)

print(" ")

# If we do not want start from 0 we can indicate where we want to start the sequence. In this example we want the start variable to be 5 and the stop variable to be 10. Note that the list will go from 5 to 9. Let's create a range less than 10

# range(start,stop)
# example:
for i in range(5, 10):
    print(i)

print(" ")

# If you do not want to increment by 1 then you can indicate how you want to step or increment each item. 
 
# range(start,stop,step)
# example:
for i in range(0, 10, 3):
    print(i)

print(" ")

# Assume that we want to write code to calculate the total of all even numbers up to 100. 

# First, we will set the total to need to have a place to collect the total and make it 0 so that we do not have anything in that. Then we write the for loop to go through all the numbers. First we need an iterating variable that would change during each iteration. We use counter for that. Then we need to get a sequence of even  numbers generated. We get the help from range function where we start at 0, stop at 101 and step through in 2.  Next we need to add the counter to the existing total. Note on this line of code the old value of total and the counter that is in the right hand side will be given to the left hand side total and it will be used in the next iteration of the loop. Finally after we finish the loop, we need a print the total.

total = 0
for counter in range(0, 101, 2):
    total = total + counter
print("Total of even numbers upto 100 :", total)
print(" ")

# Play around the code and try to see if you can change the given code example to add all the odd numbers beetween 0 and 100. Or the even numbers between 100 to 200, etc. More you try your will learn. IT is hard to learn python by reading. You need to try coding!

# Total of odd numbers upto 100
total2 = 0
for counter2 in range(1, 100, 2):
    total2 = total2 + counter2
print("Total of odd numbers upto 100 :", total2)
print(" ")

# Total of even numbers between 100 to 200
total3 = 0
for counter3 in range(100, 201, 2):
    total3 = total3 + counter3
print("Total of even numbers between 100 to 200 :", total3)