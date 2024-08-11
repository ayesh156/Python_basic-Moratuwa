# Accessing Values in a List

# A typical list will contain multiple values. To access the values in a list, the first step is to locate the values. Suppose you go to a library and you need to tell the librarian which book you need. Assume that the books are organized on shelves. First, you should specify the shelf where the book is located. Second, you should specify the location of the book on the shelf (e.g., the second book from the left). Accessing the values in a list is similar to that. 

# To locate the values in a list, the lists in Python are indexed. Consider the following Python list.

values = [15, 20, 96, 32, 17]

# Two important properties of indexing are,

    # The index of the first value is 0 (not 1).
        # In Figure 1, the first value 15 is indexed 0.
    # The values are indexed from left to right
        # In Figure 1, the first value 15 is indexed 0, the second value 20 is indexed 1, and the third value 96 is indexed 2.

# The following Python code illustrates how to access the values in a list.

values = [15, 20, 96, 32, 17]

print(values[0])
print(values[4])

# In addition to accessing a single value at a time, Python also allows extracting a section of values from a list. The following code illustrates how it is achieved.

values = [15, 20, 96, 32, 17]

print(values[0:3])
print(values[2:5])

# It is evident from the above examples that if the specified index range is [m:n], the values considered are from index m to index (n-1). For example, values[0:3] considers the values from 15 to 96 where 15 is at index 0 and 96 is at index 2 (not 3).