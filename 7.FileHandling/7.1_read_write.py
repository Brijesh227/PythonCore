# File handling:
#   File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.
#   Access external files like .txt, .csv, .json, etc.
#   Process large files efficiently without using much memory.

# check file properties:
f = open("sample.txt", "r")     # by default read mode("r")
#   filename.txt: name (or path) of the file to be opened.
#   mode: mode in which you want to open the file (read, write, append, etc.).
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


