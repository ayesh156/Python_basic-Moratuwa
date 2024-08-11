# Remove elements form a set

# 1. Using remove() method or discard() method

# Elements can be removed from the Set by using built-in remove() function but a KeyError arises if element doesn’t exist in the set. To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set, it remains unchanged

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)


print("\nSet after Removal of the two elements: ")


set1.discard(8)
set1.discard(9)
print("\nSet after discarding two elements: ")
print(set1)

for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)

# 2. Using pop() method

# Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set. 

# Note – If the set is unordered then there’s no such way to determine which element is popped by using the pop() function.

set2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("initial Set: ")
print(set2)

# Removing element from the
# Set using the pop() method
set2.pop()
print("\nSet after popping an element: ")
print(set2)