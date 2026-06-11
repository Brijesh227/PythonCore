# Iterator in python:
#   An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, which involves two key methods:
#        __iter__(): Returns the iterator object itself.
#        __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

# Need For Iterators
#    Lazy Evaluation: Processes items only when needed, saving memory.
#    Generator Integration: Pairs well with generators and functional tools.
#    Stateful Traversal: Keeps track of where it left off.
#    Uniform Looping: Same for loop works for lists, strings and more.
#    Composable Logic: Easily build complex pipelines using tools like itertools.

# Built-in Iterator:
#   strings, lists, tuples, and dictionaries.

# Iterable: list
numbers = [1, 2, 3]

# Iterator: created using iter()
it = iter(numbers)
print(next(it)) 
print(next(it))  
print(next(it))

# Custom Iterator:

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2

    def __iter__(self):     # This method should return the iterator object itself. This is usually as simple as returning self.
        return self

    def __next__(self):     # This method should provide the next item in the sequence each time it's called.
        if self.n > self.limit:
            raise StopIteration

        x = self.n
        self.n += 2
        return x


# Create an iterator for even numbers up to 10
even = EvenNumbers(10)

for num in even:
    print(num)