# A sequence is an ordered collection of elements. It is called ordered because the elements will be maintained in a specific order and the order will not change. Consider the following example.

# The variable ‘sample’ contains the string “computer”. Then we create a list with these letters. When we print the list, you can see that the list keeps the letters in the same order as the input.

sample = "computer"
my_list = list(sample)
print(my_list)

# Next, we create a set, which is another data type in Python, with these same letters. When we print the set, you can see that the letters are in a completely different order. 

my_set = set(sample)
print(my_set)

# Therefore, list is categorized as an ordered data type and set as an unordered data type.

# Three basic sequence data types in Python are list, tuple, and range. In our first course Python for Beginners, we learned about the list data structure. In this lesson, we will discuss the tuple data structure in detail, which is very similar to lists.