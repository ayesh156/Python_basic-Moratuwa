# Selecting the Loop

# The ‘for’ loop is generally used when the number of iterations or the sequence can be identified at program compilation or before execution of loop.
# The ‘while’ loop can be used for any other situations.

## Nested Loops

# We can also have nested loops. We can put a loop inside a loop to make a nested loop. The syntax is as given where we indent the loop inside the out loop. When we execute for each iteration of the outer loop the entire inner loop will be iterated. Once it is finished it will go to the outer loop and take the next iterating variable from the outer loop and once again completely execute the inner loop iteration. We call it nesting because we put a loop inside another loop. We can have any number of loops insides loop. For example we can have a loop inside a loop inside another loop. Note if each loop is long it will take a long time to complete all the nested loops.

#  for iterating_var in sequence:
#     while expression:
#          statement(s)
#          statement(s)
#     statement(s)

# We can also have different combinations when nesting loops.  We can have for and while as in the last example or while and for as given in this example or even while and a while or for and a for loop. Any combination of loops are possible and any number of nesting levels are also possible.

# Here is an example for a nested loop. If we look at the example we can think about printing one line of characters by using a for loop that goes from 0 to 9. Now we want to have all 5 lines. So we put another loop outside this loop to go from 0 to 4 iterating 5 times. This will print 5 lines.

# outer loop
for x in range(5):
    # inner loop
    for y in range(10):
        print("$",end='')
    print('')

j = 0
# outer loop
for i in range(6):
    while (j < i):
        print('*'*i, end='')
        j = j + 1
    print('')
