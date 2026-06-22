# -------------------
# Use with command
#   - which automatically handles closing. This reduces the risk of file corruption and resource leakage.
# -------------------


# File handling:
#   File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.
#   Access external files like .txt, .csv, .json, etc.
#   Process large files efficiently without using much memory.

# check file properties:
f = open("sample.txt", "r")     # not recommended way to open file(sample.txt might be not accessebile at global level)
#   filename.txt: name (or path) of the file to be opened.
#   mode: mode in which you want to open the file (read, write, append, etc.).
#         "r" mode is default mode

print("Filename:", f.name)      # Filename: sample.txt
print("Mode:", f.mode)          # Mode: r
print("Is Closed?", f.closed)   # Is Closed? False

f.close()
print("Is Closed?", f.closed)   # Is Closed? True

# Reading a File
#   file.read()         =>  Reads the entire file as a single string. After reading, it’s good practice to close the file to free up system resources.
#   file.readline()     =>  Reads one line at a time. 
#                           It is helpful when working with large files, 
#                           as it reads data line by line instead of loading the entire file into memory.
#                       file.readline(7) => Hello w
#                           It has read size characters, or
#                           It reaches the newline character (\n) at the end of the line.
#   file.readlines()    =>  Reads all lines and returns them as a list  

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# Hello world
# python program
# 123 456

with open("sample.txt", "r") as file:
    line = file.readline()
    print(line)  #  Hello world     #Prints the first line of the file

    while True:
        line = file.readline()
        if not line:
            break  # Stop when end of file is reached
        print(line.strip())

    line = file.readline(12)        
    print(line)                 # Hello world and extra line break (because print() adds its own newline after printing the string, and the string already contains \n.)

    lines = file.readline()     # ['Hello world\n', 'python program\n', '123 456']

# Writing a file

# Writing to a file (overwrites if file exists)
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")