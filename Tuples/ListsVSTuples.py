# Lists vs Tuples

# Lists and tuples are very similar to each other. However, lists are more versatile than tuples. You can update the values in a list and expand or shrink a list. But you cannot do any of those with a tuple. On top of that lists have more built-in functions than tuples.

# Since lists have all these advantages over tuples, how are tuples useful? Tuples are memory efficient than lists which means they consume less memory.

import sys
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

# Let us create a tuple and a list that contain the same set of elements and measure the amount of memory consumed by each of them. We will use a python function called getsizeof(). It will return the amount of memory consumed in bytes. To use this function, we need the sys module. Hence, sys module is imported. When we run sys.getsizeof(my_list), we get the output 120. Which means our list has consumed 120 bytes of memory. Let us do the same for our tuple as well. We can see that it has consumed only 80 bytes of memory which is 15% less compared to the list.

# If the data need not to be changed in the future, use tuples since it will save a significant amount of memory. If the data needs to be modified in the future, you must use lists since tuples are immutable.