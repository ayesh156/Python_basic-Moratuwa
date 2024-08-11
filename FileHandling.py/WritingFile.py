# Writing to a file

# To write to a file, we have to open the file in write mode. To do that, we can spec the mode as “w” while calling the open function. Once opened, we can use the function write() to write a given string to the file.

fhandle = open("myfile.txt","w")
mystring = "Python is great.\nFile handling is so easy"
fhandle.write(mystring)

# Closing a file

# After we are done with the file operations, we should close the file we opened. Python may automatically close any opened file when the file is reassigned to a different file handle. However, it is a good programming practice to close the file after use. We can close any open file by using the close() function as shown in the example.

fhandle.close()