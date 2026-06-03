# ----

#   self is must in __init__ and instance method.

#----

# Class:
#     Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.  

#     Attributes are the variables that belong to a class.
#     Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute

    def show(self):
        print(self.name, self.age)      # tommy 12
        print(self.species)             # Canine
        print(Dog.species)              # Canine
        print(species)                  # error
        
d1 = Dog("tommy", 12)

d1.show()   
print(Dog.species)                      # Canine

# Attributes:
#     species is a class attribute, meaning it is shared by all instances of the class.

# constructor(__init__):
#     __init__() is a constructor method that runs automatically when a new object is created. 
#     It is used to initialize object data.

# self:
#     self refers to the current object, allowing each object to store and access its own data.
#     self.name and self.age are instance attributes, unique to each Dog object created from the class.
#     when defining methods inside a class, first parameter is always self. 

class Test:
    def show():
        print("Hello")
t = Test()
t.show()        # TypeError: Test.show() takes 0 positional arguments but 1 was given


# Object:
#     An Object is an instance of a Class.

#     State: represented by the attributes and reflects the properties of an object.
#     Behavior: represented by the methods of an object and reflects the response of an object to other objects.
#     Identity: gives a unique name to an object and enables one object to interact with other objects.