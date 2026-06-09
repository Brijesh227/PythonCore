# The dir() function returns an alphabetized list of all valid attributes and methods. 
# This includes user-defined variables, class methods, and built-in "dunder" (double underscore) attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Tesla", "Model S")
print(dir(my_car))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', 'brand', 'model']