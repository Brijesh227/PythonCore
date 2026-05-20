# Arguments => actual value passed to a function
# Parameters => variable in the declaration of function

# 'name' is the PARAMETER (the placeholder)
def greet(name):
    print(f"Hello, {name}!")

# "Alice" is the ARGUMENT (the actual value)
greet("Alice")

# ----------------------

# *args vs **kwargs
#   *args collects extra positional arguments as a tuple.
#   **kwargs collects extra keyword arguments as a dictionary.

#   you can't put *args after **kwargs in the function definition   # SyntaxError

# standard arguments list

#   Standard positional arguments (e.g., arg1, arg2)
#   Variable positional arguments (*args)
#   Keyword-only arguments (e.g., key=value)
#   Variable keyword arguments (**kwargs) 


# ---------------------

# pass => used to keep code blocks valid where a statement is required but no logic is needed yet.
# code after pass will be executed as normal no skip 