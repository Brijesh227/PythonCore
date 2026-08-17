# List comprehension: 
#   List comprehension is a way to create lists using a concise syntax. 
#   new_list = [expression for item in iterable if condition]


li = [2, 3, 9]
li = [[item for item in [li]] for i in range(3)]
print(li)       # [[[2, 3, 9]], [[2, 3, 9]], [[2, 3, 9]]]

li = [[item for item in li] for i in range(3)]
print(li)       # [[2, 3, 9], [2, 3, 9], [2, 3, 9]]

# find what is return

a = ['python', 'java', 'golang']
b = [i[0].upper() for i in a]
print(b)        # ['P', 'J', 'G']

# Dictionary Comprehension:

my_dict = {i: i**2 for i in range(1, 4)}
print(my_dict)      # {1: 1, 2: 4, 3: 9}

# Tuple Comprehension:

#   When you use parentheses with a comprehension, Python actually creates a generator expression, not a tuple. 
#   To get a tuple, you must either convert the generator with tuple() or define a tuple literal directly.

# Generator expression (not a tuple)
my_gen = (i for i in range(1, 10))
print(my_gen)       # <generator object <genexpr> ...>

# Converting generator to tuple
my_tuple = tuple(i for i in range(1, 10))
print(my_tuple)     # (1, 2, 3, 4, 5, 6, 7, 8, 9)
