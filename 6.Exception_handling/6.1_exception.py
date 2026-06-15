# Error(compile time.): 
#   Issues in the program logic such as SyntaxError, etc. It occurs at compile time.
# Exception (runtime): 
#   Problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).


# why exception handling:
#   Handles runtime errors such as invalid input, file not found, division by zero and type mismatches that occur during program execution.
#   Helps improve program reliability by ensuring the application does not terminate unexpectedly when an error occurs.


# syntax:
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

# BaseException => root of Python's exception hierarchy. All other exceptions directly or indirectly inherit from it.
# Exception     => Exception class is the base for all non-exit exceptions. 
#                   Handle application error not system error see below heirarchy

# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# └── Exception
#     ├── ArithmeticError
#     │   ├── ZeroDivisionError
#     │   ├── OverflowError
#     │   └── FloatingPointError
#     │
#     └── TypeError

try:
    raise Exception("This is a generic exception")
except Exception as e:      # don't use BaseException else some cases like ctrl+c(KeyboardInterrupt) is handled and program keep on running.
    print(e)

# AttributeError    => AttributeError occurs when you try to access or assign an attribute that does not exist for an object.
class MyClass:
    pass

obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)

# OSError(IOError)      => Raised when a system-related operation (like file I/O, opening files, or interacting with the OS) fails
#       IOError is just an alias for OSError (they are the same).
#       FileNotFoundError is a subclass of OSError, specifically raised when a file or directory does not exist.

# TypeError	    => Raised when an operation or function is applied to an object of inappropriate type 
#                   (e.g., adding a string to an integer).
# ValueError	=> Raised when a function receives an argument of the correct type but with an invalid value 
#                   (e.g., converting "abc" to an integer).

# Multiple Exception
a = ["10", "twenty", 30]
try:
    # 'twenty' cannot be converted to int
    total = int(a[0]) + int(a[1])  
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")

# catch-all

try:
    res = "100" / 20 
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")