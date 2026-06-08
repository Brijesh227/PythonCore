# polymorphism: 
#       same name different behaviour
#       Overriding(Run time): Child class provides its own version of that method(below code)
#       Overloading (Compile time): same function name, different parameter count/types

# Overloading:(Compile time)
#   - Python does NOT support true method overloading directly. If you define same function again, old one gets replaced.
#   - Languages like Java or C++ support this. But Python doesn’t because it’s dynamically typed 
#   - Python does not support true compile-time polymorphism because method calls are resolved at runtime. 
#     However, similar behavior can be achieved using default arguments, variable-length arguments (*args), or keyword arguments (**kwargs).

# --- patch for overlaoding -----
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))


# Overriding(Run time):
#   - Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.    

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_car(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrole or diesel"           

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_car = Car("tata", "nexon")
print(my_car.fuel_type())       # petrole or diesel

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())     # Electric charge


# Polymorphism in Built-in Functions
#   - Python’s built-in functions like len() and max() are polymorphic because they work with different data types and return results based on type of object passed. 
#   - This showcases it's dynamic nature, where same function name adapts its behavior depending on input.

print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings

#   - operator like + will convert into __add__() so int and str method implement it's own method 
#     (https://chatgpt.com/share/6a167be7-bff0-8324-95d7-855b0666cdff)

print(2 + 3)          # addition
print("Hi " + "Bro")  # concatenation

# python internal working:
# a + b -> a.__add__(b)
class int:
    def __add__(self, other):
        return numeric_addition
    
class str:
    def __add__(self, other):
        return string_concatenation