# append: Adds the entire object as a single element to the end of the list.

letters = ['a', 'b']
letters.extend("xyz")
print(letters)      # ['a', 'b', 'x', 'y', 'z']

# extend: 
#   - Takes an iterable and adds each element individually to the list.
#   - Add one level nesting only

letters = ['a', 'b']
letters.append("xyz")
print(letters)      # ['a', 'b', 'xyz']

a = [1, 2]
a.extend([3, [4, 5]])
print(a)            # [1, 2, 3, [4, 5]]

# '+' behaves like extend but 
#   + creates new list and 
#   extend modified exisiting list

a = [1, 2]
b = [3, 4]

c = a + b       # [1, 2, 3, 4] (new list)