# The pass Keyword

# Pass does not change the loop execution but it can be used to do nothing in a loop. In a loop we cannot have an empty block of code inside a loop. So we can use the pass to write some code with loop that does nothing.

# In this example we have list of fruits. At the moment we do not know what to do with them but we want to have loop so that we would not forget to do something with the fruits later. If we write the code without any executable code for the loop body other than the comment it will give a syntax error.

# How we can avoid that is to put a pass statement inside the loop. And later when we know what to do with the fruits inside the loop we can remove the pass and put some code there.

fruits = ['Apple', 'Orange', 'Mango', 'Banana']
for fruit in fruits:
    # Not sure what to do!
    pass
print('Done')