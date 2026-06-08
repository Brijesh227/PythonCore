# inheritance: 
#   - allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.full_name())

# ---------------------------

# Method resolution order:
#   - The order in which base classes are searched when looking for an attribute in multiple inheritance. 
#   - It follows a linearization rule: 
#       the current class is checked first, then parent classes are searched from left to right, each class only once.

# Class.mro() -> returns a list
# Class.__mro__ -> returns a tuple

# The mro() and __mro__ outputs show the search order: Class4 -> Class2 -> Class3 -> Class1 -> object

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
     
print(Class4.mro())         # [<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.Class3'>, <class '__main__.Class1'>, <class 'object'>]
print(Class4.__mro__)       # (<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.Class3'>, <class '__main__.Class1'>, <class 'object'>)

# but when you use super it prevents duplicate calls of the same method.

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
     
obj = Class4()
obj.m()

# In Class4
# In Class2
# In Class3 
# In Class1     // no duplicate


# when override in both class but child defination has pass

class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")  
       
class Class4(Class2, Class3):
    pass   
    
obj = Class4()
obj.m()         # In Class2

# all have same method:

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")

obj = Class4()      # In Class4
obj.m()
Class2.m(obj)       # In Class2
Class3.m(obj)       # In Class3
Class1.m(obj)       # In Class1
