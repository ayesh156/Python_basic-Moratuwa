# File handling errors

# When opening files, we need to specify the file name, like we saw in the examples. This will only work if the file is located in the current working directory.

# If we want to open a file which is located at a location different from our working directory, we should give the full file path as the file name.

# Whatever the mode that we try to open the file with, you can encounter a situation in which the file you are trying to open does not exist in the specified file path or the current directory.

# In such a situation, depending on the file opening mode, python will take different actions.

# If the file open mode is r, or read, python will show an error saying that the file cannot be found.

# If the file open mode is w, or write, python will create a new file named with filename specified if it does not already exist.