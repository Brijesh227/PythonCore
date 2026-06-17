# -------------------
# Use with command
# -------------------


# File handling:
#   File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.
#   Access external files like .txt, .csv, .json, etc.
#   Process large files efficiently without using much memory.

# check file properties:
f = open("sample.txt", "r")     # not recommended way to open file, depends on from where file executes
#   filename.txt: name (or path) of the file to be opened.
#   mode: mode in which you want to open the file (read, write, append, etc.).
#         "r" mode is default mode

print("Filename:", f.name)      # Filename: sample.txt
print("Mode:", f.mode)          # Mode: r
print("Is Closed?", f.closed)   # Is Closed? False

f.close()
print("Is Closed?", f.closed)   # Is Closed? True

# Reading a File
#   file.read() which reads the entire content of the file. After reading, it’s good practice to close the file to free up system resources.

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# Hello world
# python program
# 123 456

# Writing a file

# Writing to a file (overwrites if file exists)
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

# Use with statement which automatically handles closing. This reduces the risk of file corruption and resource leakage.

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)