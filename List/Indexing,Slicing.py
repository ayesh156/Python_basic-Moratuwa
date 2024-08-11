# Indexing and Slicing

# We learned earlier that indices are required to access values in a list. This section summarizes indexing and introduces an alternative way of indexing called negative indices

# Negative Indices

# Figure 4 illustrates how the list L is indexed using normal indexing and negative indexing.

L = ['a', 'b', 'c']

# In negative indexing, the last value of the list is indexed -1, similar to how the first value is indexed 0 in normal indexing. The rest of the elements are indexed from right to left. In the given example, the last element ‘c’ is indexed -1, the next value to the left ‘b’ is indexed -2, and ‘a’ is indexed -3. Therefore, ‘print(L[-2])’ will output ‘b’.

print(L[-2])

# Slicing

# Slicing means extracting a part of the list. Using the range m to n within square brackets (L[m:n]) will consider the values from index m to index (n-1). In addition to what has been discussed in previous sections, the second part of the range is empty in L[1:]. It means from index 1 up to the last value of the list. Hence,  L[1:] outputs the values ‘b’ and ‘c’. 

print(L[1:])

# Practice Exercise 2

# Complete the following code to print all the even numbers in the list (numList)

numList = [2, 4, 6, 8, 3, 4, 2, 1]

evenList = []

for i in numList:
    if (i % 2 == 0) and (i not in evenList):
        evenList.append(i)

print(evenList)