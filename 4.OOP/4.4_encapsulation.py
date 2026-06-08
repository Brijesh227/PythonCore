# Python does not have true private variables like Java or C++. it's doing name mangling
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

# ------------------

# Encapculate brand variable, make it private(__varname)
# private => access within class but object can't access it.

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

print(User._User__company)    # if we remove _User then we can't access it, AttributeError: type object 'User' has no attribute '__company'