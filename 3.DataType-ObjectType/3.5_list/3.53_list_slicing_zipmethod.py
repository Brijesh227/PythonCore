# slicing creates a brand-new list object in memory. 

a = ['Python', 'Java', 'C++', 'Go']
b = a       # refers to same list
c = a[:]    # create new reference(it shallow copy not deep copy)

print(a)    # ['Python', 'Java', 'C++', 'Go']
print(b)    # ['Python', 'Java', 'C++', 'Go']
print(c)    # ['Python', 'Java', 'C++', 'Go']

b[0] = 'Code'
c[1] = 'Quiz'

print(a)    # ['Code', 'Java', 'C++', 'Go']
print(b)    # ['Code', 'Java', 'C++', 'Go']
print(c)    # ['Python', 'Quiz', 'C++', 'Go']

# shallow copy in list

original = [[1, 2], [3, 4]]
sliced_copy = original[:]

# Modifying a shared inner object
sliced_copy[0][0] = 99

print(original)     # Output: [[99, 2], [3, 4]] 
print(sliced_copy)  # Output: [[99, 2], [3, 4]]

# ----

li = ['a', 'b', 'c', 'd', 'e']
print(li[10:])      # []

# multiplication in list

li = ['a', 'b', 'c'] * 2
print(li)       # ['a', 'b', 'c', 'a', 'b', 'c']

li = ['a', 'b', 'c'] * -2
print(li)       # []


# zip combines elements from multiple iterables (like lists, tuples, or strings) into a single iterator of tuples. 

a = [10, 20, 30, 40]
b = [1, 2, 3, 4]

res = zip(a,b)
print(list(res)) 

# [(10, 1), (20, 2), (30, 3), (40, 4)]

