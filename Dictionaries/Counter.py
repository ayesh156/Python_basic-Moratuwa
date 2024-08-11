# A List of names with possible duplicate entries, is given
# Find the unique names and the number of times each name appears in the List

names = ['Amal', 'Kamal', 'Sunil', 'Saman', 'Amal', 'Amal', 'Saman', 'Nimal', 'Kamal', 'Ajith', 'Kamal', 'Saman', 'Nimal', 'Kamal', 'Sunil', 'Sarath']

counts = dict() # create empty dictionary

for name in names: # iterate through the names List
    if name not in counts: # checking if the name isalready in the dict
        counts[name] = 1 # add new element to the dict with value 1
    else:
        counts[name] = counts[name] + 1 # increment the value by 1

print(counts) # finally print the dict