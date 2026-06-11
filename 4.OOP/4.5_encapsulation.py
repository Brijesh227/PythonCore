# Python does not have true private variables like Java or C++. it's doing name mangling
# it follows naming conventions and uses a technique called name mangling to support encapsulation.
# https://chatgpt.com/share/6a17d38a-8ef8-8322-af9d-021eac08ab46

class User:
    def __init__(self, name):
        self.__name = name

# what python does (Name mangling)
# self._User__name

u = User("A")

# actually stores: 
#  u.__dict__ as
# {
#     '_User__name': 'A'
# }

# it's just stored with _User__name that's why it can't directly accessible but with u._User__name you can access it.
print(u._User__name)    # A

# -------------------------------------------------------

# private 
#       => Private members are variables or methods that cannot be accessed directly from outside the class. 
#       => access within class but object can't access it.

# Object level private variable
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

# class level private variable
# access pattern: ClassName._Class__var
class User:
    __company = "OpenAI"   # class-level private variable

print(User._User__company)      # OpenAI 
print(User.__company)           # AttributeError: type object 'User' has no attribute '__company'


# you can access protected and private member by it's public method(getter) and modify that using setter method

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())

# -------------------------------------------------------

# public
#    - by default all public

class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible 

# -------------------------------------------------------

# protected
#       - Protected members are variables or methods that are intended to be accessed only within the class, it's object and its subclasses

class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass
        
e = Employee('john', 20)
emp = SubEmployee("Ross", 30)
print(e.name)           # john
print(e._age)           # 20
print(e.__dict__)       # {'name': 'john', '_age': 20}
print(emp.name)         # Ross
print(emp._age)         # 30
print(emp.__dict__)     # {'name': 'Ross', '_age': 30}
emp.show_age()          # Age: 30 