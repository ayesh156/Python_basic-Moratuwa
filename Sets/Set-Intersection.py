# Set Intersection

# The intersection() method returns a set that contains the similarity between two or more sets.

# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

# Python also provides you with the set intersection operator (&) that allows you to intersect two or more sets.

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)
print(result)

print(x&y)