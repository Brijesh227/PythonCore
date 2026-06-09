# class variable that track numbers of cars created.

# my solution (wrong)
class Car:
    car_number = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.car_number += 1    

        # self.car_number creates an instance variable named car_number for each object instead of modifying the class variable.
        # So each object starts from the class value 0, increments to 1, and stores its own copy.
        print(f"number: {self.car_number}")     # always 1

my_car1 = Car("tata", "nexon")
my_car2 = Car("mahindra", "xuv")

print(Car.car_number)           # 0              


# right solution
class Car:
    car_number = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_number += 1 

my_car1 = Car("tata", "nexon")
my_car2 = Car("mahindra", "xuv")

print(Car.car_number)           # 2
