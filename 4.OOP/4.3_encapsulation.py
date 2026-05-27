# Encapculate brand variable, make it private(__varname)
# private => access within class but object can't access it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_car(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"  


my_car = Car("tata", "nexon")
# print(my_car.__brand)         # AttributeError: 'Car' object has no attribute '__brand'
print(my_car.get_car())         # tata              

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.full_name())     