# Dunder method:
#   A special methods whose names start and end with double underscores.
#   They are also called:
#       Magic Methods
#       Operator Overloading Methods

# pyhthon internally translates these operations into dunder method calls.

len(my_list)    => my_list.__len__()
a + b           => a.__add__(b)
print(obj)      => obj.__str__()

# core idea:
class Student:
    def __len__(self):
        return 100

s = Student()

print(len(s))       # 100  becuase s.__len__() called

# commonly used

# __init__
class User:
    def __init__(self, name):
        self.name = name

u = User("John")        

# internal working
# u = User.__new__(User)
# u.__init__("John")


# __str__
class User:
    def __str__(self):
        return "User Object"

u = User()

print(u)
print(str(u))

# | Python Syntax  | Dunder Method           |
# | -------------- | ----------------------- |
# | `obj + x`      | `obj.__add__(x)`        |
# | `obj == x`     | `obj.__eq__(x)`         |
# | `len(obj)`     | `obj.__len__()`         |
# | `print(obj)`   | `obj.__str__()`         |
# | `obj[i]`       | `obj.__getitem__(i)`    |
# | `obj[i] = x`   | `obj.__setitem__(i, x)` |
# | `x in obj`     | `obj.__contains__(x)`   |
# | `for x in obj` | `obj.__iter__()`        |
# | `obj()`        | `obj.__call__()`        |
