# with statement:
#   The with statement simplifies resource management by automatically handling setup and cleanup, 
#   ensuring files or connections close safely even if errors occur.

# without with 
# file = open("example.txt", "r")
# try:
#     content = file.read()
#     print(content)
# finally:
#     file.close()  # Ensures the file is closed

# with automatically
with open("sample.txt", "r") as file:
    content = file.readlines()
    print(content)  # File closes automatically