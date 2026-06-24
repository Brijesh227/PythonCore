# Iterator: https://www.youtube.com/watch?v=pH7YVRhnpUI
# Generator: https://youtu.be/ZfJoU67tG1A?si=ld2VPCMBqO7i0b9_

# Iterable: 
#   Iterable is object, which one can iterate over.
#   It must have __iter__ method that returns Iterator
#   E.g., list, string, tuple and dictionary.

# Iterator:
#   An iterator is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. 
#   It follows the iterator protocol, which involves two key methods:
#        __iter__(): Returns the iterator object itself.
#        __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.
#   Iterator <-- used by --> for loop

#   Need For Iterators
#    Lazy Evaluation: Processes items only when needed, saving memory.(load one element at a time)
#    Generator Integration: Pairs well with generators and functional tools.
#    Stateful Traversal: Keeps track of where it left off.
#    Uniform Looping: Same for loop works for lists, strings and more.


# point to remember:
#   every iterator is also iterable
#   Not all Iterables are Iterator

numbers = [1, 2, 3]

# Iterator: created using iter()
it = iter(numbers)
print(next(it)) 
print(next(it))  
print(next(it))


# custom Iterable:
class CustomIterable:
    def __init__(self, start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return customIterator(self)  

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


# Generator is another(abstact) way of crearing itertor, just write yield

def get_even_number(num):
    if num % 2 == 0:
        yield num 

for i in range(1, 10):
    result = get_even_number(i)
    if result is not None:
        print(result)

# ----- OR --------

def get_even_number(num):
    for i in range(1,num):
        if i % 2 == 0:
            yield i

for i in get_even_number(10):
    print(i)


# generator in sigle line:
nums = (x*x for x in range(1000000))