# list comprehension: 
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