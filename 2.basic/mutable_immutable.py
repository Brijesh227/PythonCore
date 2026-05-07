# simply when we create new variable it created as object in python and assign memory location to that variable.
# immutable: Integers, floats, boolean, strings, and tuples are immutable in Python. This means that once you create an object of these types, you cannot change its value. If you try to modify it, a new object will be created in memory with the new value.
# mutable: Lists, dictionaries, and sets are mutable in Python. This means that you can change their contents without creating a new object. When you modify a mutable object, it changes the original object in memory.

username = "abc"

# immutable meaning here:
#    "abc" string(object in python) is stored in memory and username is pointing to that memory location.

username = "def"  # this is valid

# when we assign "def" to username, it creates a new string object in memory and username now points to the new memory location where "def" is stored. 
# The original string "abc" remains unchanged in memory, and if there are no other references to it, it may eventually be garbage collected by Python's memory management system.

x = 10
y = x  # y is now pointing to the same memory location as x
x = 20  # new memory location created having value 20, x now points to a new memory location, while y still points to the original memory location with the value 10
print(x)  # Output: 20
print(y)  # Output: 10


