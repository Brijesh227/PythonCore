# a = lambda x: x + 1
    # a = function name
    # x = Argument
    # x + 1 = Return value

# upper case using lambda function
a = 'GeeksforGeeks'
upper = lambda x: x.upper()  
print(upper(a))

# lambda function with filter() function
c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))                       # see filter object is converted to list

# lambda function default argument(arg = x) that's why i() is used.
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())
