# Set Union

# The union() method returns a set that contains all items from the original set, and all items from the specified set(s). You can specify as many sets you want, separated by commas. It does not have to be a set, it can be any iterable object. If an item is present in more than one set, the result will contain only one appearance of this item.

# Furthermore, Python provides you with the set union operator | that allows you to union two sets

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)

print(x|y)