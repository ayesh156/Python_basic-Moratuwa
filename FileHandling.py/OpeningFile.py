# File Handling with Python

# Files help us store our data and information in a persistent way on a computer. The main memory (or RAM) is a volatile memory that loses its data when power is switched off. In contrast, files are stored in secondary storage devices such as hard disks, ssds, pen drives etc., and the data stored in files are not lost when the power goes off.

# File types 

# There are many file types available, probably thousands, that store different types of data. For example text files store a sequence of lines consisting of characters such as letters, numbers, and special characters. PDFs, word documents, excel spreadsheets, image files, and video files are some examples of file types.

# A file is identified by its name and the extension. Extension is the last part of a file name which is written with a dot and few characters. For example .txt is the extension for text files. If we assume our file name is myfile.txt, myfile is the name of the file and .txt is the extension.

# Opening a file

# Before performing any file operations on a file, the file needs to be opened. The open() function in python facilitates opening files in Python. Open function opens the required file and provides us with a special pointer called a file handle. A file handle is a special variable that links our python program to the file and helps us perform various file operations.

# While opening files, Python allows us to specify a file opening mode, which indicates the purpose of opening the file. For example, we can tell python that we want to open a file only for reading or for both reading and writing.

# To open a file, you must provide the name of the file that you want to open as a string. In addition to the file name, you can also optionally specify the file opening mode. There are many file opening modes. The simplest opening modes are read ‘r’ and write ‘w’, which opens the file for reading and writing, respectively.

fhandle = open("myfile.txt")

fhandle = open("myfile.txt","r")