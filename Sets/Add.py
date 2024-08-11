# Adding elements to a set

# 1. Using add() method

# Elements can be added to the Set by using built-in add() function. Only one element at a time can be added to the set by using add() method, loops are used to add multiple elements at a time with the use of add() method.

# Note – Lists cannot be added to a set as elements because Lists are not hashable whereas Tuples can be added because tuples are immutable and hence Hashable.

set1 = set()
print("Initial blank Set: ")


# Adding element and touple to the Set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after addition of Three elements: ")
print(set1)

# Adding elements to the Set
# using Iterator
for i in range(1,5):
    set1.add(i)
print("\nSet after addition of elements from 1-5: ")
print(set1)

# 2. Using update() method

# For addition of two or more elements the Update() method is used. The update() method accepts lists, strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.

set2 = set([4,5,(6,7)])

set2.update([10, 11])

print("\nSet after Addition of elements using Update: ")
print(set2)