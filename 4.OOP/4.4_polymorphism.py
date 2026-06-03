# polymorphism: 
#       same name different behaviour
#       Overriding(compile time): Child class provides its own version of that method(below code)
#       Overloading (Run time): same function name, different parameter count/types

# Python does NOT support true method overloading directly. If you define same function again, old one gets replaced.

# Languages like Java or C++ support this. But Python doesn’t because it’s dynamically typed 
#   it resolves method calls at runtime, not during compilation. So, true method overloading isn’t supported, 
#   though similar behavior can be achieved using default or variable arguments.

# + operator will convert into __add__() so int and str method implement it's own method (https://chatgpt.com/share/6a167be7-bff0-8324-95d7-855b0666cdff)
# Python’s built-in functions like len() and max() are polymorphic they work with different data types and return results based on type of object passed. 
#   This showcases it's dynamic nature, where same function name adapts its behavior depending on input.


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