# [expression for item in iterable if condition]


# even number
l1 = [1,2,3,4]

even = lambda x: x % 2 == 0
l1 = [i for i in l1 if even(i)]
print(l1)