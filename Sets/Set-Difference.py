# Set Difference

# The difference() method returns a set that contains the difference between two sets.

# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

# You can also find the set difference using - operator in Python.

A = {"a", "b", "c", "d"}
B = {"c", "f", "g"}

# Difference to B-A
print(A.difference(B))

print(B-A)
print(A-B)