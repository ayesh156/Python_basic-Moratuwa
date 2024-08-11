# Reading a file

# After opening the file, the file content can be read using various python functions. read() function reads the whole file at once whereas the readline() function reads the file line by line. To read a file, the file should be opened in read mode and the opened file should be assigned to a file handle. While opening a file, if a mode is not explicitly specified, Python opens the file in read mode.

fhandle = open("myfile.txt")
fcontents = fhandle.read()
print(fcontents)

# While performing file operations that deal with files line by line, such as the readline() function, Python identifies the end of each line by a special character called the newline character. Newline character is written as “\n” and is placed at the end of each line. While printing a sequence of characters, whenever a newline character is encountered, python goes to the next line before printing the next character.

fhandle = open("myfile.txt")
print(fhandle.readline())
print(fhandle.readline())
print(fhandle.readline())
