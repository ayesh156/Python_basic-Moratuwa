# Accessing elements of a list

# Set items cannot be accessed by referring to an index, since sets are unordered and the items have no index. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

set1 = set(["a", "b", "c"])
print("\nInitial set")
print(set1)

# Accessing element using for loop
for i in set1:
    print(i, end=" ")

# Checking the element
# using in keyword
print("a" in set1)