# decorator: A decorator is a function that takes another function as an argument and returns a modified version of that function. 
#            It is typically used for logging, enforcing access control, instrumentation, caching and more.

# Using @decorator_name syntax
# @wrapper
# def function(n):
#     statements(s)

# Using manual function assignment syntax
# def function(n):
#     statement(s)
# function = wrapper(function)

# Simple decorator  
def deco(f):
    def inner(*args, **kwargs):
        print("before calling the function")
        res = f(*args, **kwargs)
        print("after calling the function")
        return res
    return inner

@deco
# Function to be decorated  
def add(a,b):
    return a + b

print(add(3,4))


# Simple wrapper
def deco(f):  
    def wrap():  
        print("Before execution")
        f()  
        print("After execution") 
    return wrap  

def func():  
    print("Inside function!")  

func = deco(func)  # Apply decorator  

func()  # Call decorated function

# Real world scenario:

def admin_only(f):
    def wrap(user):
        if user != "admin":
            return print("Access Denied!")
        return f(user)
    return wrap

@admin_only
def access_data(user):
    print(f"Welcome {user}, access granted.")

# Test cases
access_data("guest")    # Access Denied!
access_data("admin")    # Welcome admin, access granted.

# Cache decorator

def cache_value(func):
    cache_res_dict = {}
    def check_cache_value(*args,**kwargs):
        if args in cache_res_dict:
            print("cache here")
            return cache_res_dict[args]
        else:
            print("normal execution")
            res = func(*args,**kwargs)
            cache_res_dict[args] = res
            return res
    return check_cache_value

@cache_value
def add(a,b):
    return a + b

print(add(3,4))
print(add(3,4))

print(add(3,5))