# Variables store data in memory and scope defines the specific region of a program where a variable is accessible.

# local variable: 
#   - created when the function is called and destroyed when the function exits, 
#   - NameError for accessing outside the function.

# If a variable is not found inside a function (local scope), Python automatically looks for it in global scope. 
# However, if a local variable has same name as a global one, it will shadow global variable inside that function.

def fun():
    s += ' GFG'   # Error: Python thinks s is local
    print(s)

s = "I love GeeksforGeeks"
fun()

# UnboundLocalError: local variable 's' referenced before assignment

# ----------------------

s = "Python is great!"

def fun():
    global s
    s += " GFG"   # Modify global variable
    print(s)                                                            # Python is great! GFG
    s = "Look for GeeksforGeeks Python Section"  # Reassign global
    print(s)                                                            # Look for GeeksforGeeks Python Section

fun()
print(s)                                                                # Look for GeeksforGeeks Python Section     



# --------------------------

a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)

# global: 1
# f(): 1
# global: 1
# g(): 2
# global: 1
# h(): 3
# global: 3

