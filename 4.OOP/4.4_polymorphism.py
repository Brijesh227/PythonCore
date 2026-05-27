# polymorphism: 
#       same name different behaviour
#       Overriding: Child class provides its own version of that method(below code)
#       Overloading: same function name, different parameter count/types

# Python does NOT support true method overloading directly. If you define same function again, old one gets replaced.
# + operator will convert into __add__() so we int and str method implement it's own method (https://chatgpt.com/share/6a167be7-bff0-8324-95d7-855b0666cdff)
# java and c++ supports Overloading


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