# inner function (nested function) is a function defined inside another function. 

# They are mainly used for:

#   Encapsulation: Hiding helper logic from external access.
#   Code Organization: Grouping related functionality for cleaner code.
#   Access to Outer Variables: Inner functions can use variables of the enclosing (outer) function.
#   Closures and Decorators: Supporting advanced features like closures (functions that remember values) and function decorators.


# scope of functions: (LEGB rule)
#   - Local scope: Variables defined inside a function are only accessible within that function.
#   - Enclosing scope: In nested functions, the inner function can access variables of the outer function.
#   - Global scope: Variables defined at the top level of a script or module are accessible throughout the module.
#   - Built-in scope: Contains built-in functions and exceptions that

def fun1(): 
    msg = "Geeks for geeks"
    def fun2(): 
        print(msg) 
    fun2()
fun1()


def fun1(): 
    a = 45
    def fun2(): 
        nonlocal a      # nonlocal tells Python to use the variable 'a' from the outer scope instead of creating a new local one.
        a=54
        print(a)        # 54
    fun2()
    print(a)            # 54 because fun2 modified the nonlocal variable 'a' in fun1's scope
fun1()


# Real World Applications of Inner functions
#   - Closures: Inner functions can capture and remember the state of their enclosing scope,

#   - Decorators (Function wrappers):
#       To modify the behavior of a function or class without changing its actual code.
#       It is typically used for logging, enforcing access control, instrumentation, caching and more.
#       Inner functions are commonly used in decorators to modify the behavior of other functions.

import logging
logging.basicConfig(level=logging.INFO) 

def logger(func):                                                           # logger function defines wrapper(), which logs the function name and arguments before calling it.
    def wrapper(*args, **kwargs):                                           #  *args collects positional arguments, **kwargs collects keyword arguments, so wrapper works for any function.
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}") 
        return func(*args, **kwargs) 
    return wrapper

@logger
def add(a, b):
    return a + b  
print(add(3, 4))

# INFO:root:Executing add with arguments (3, 4), {}
# 7
