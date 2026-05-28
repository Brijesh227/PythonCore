# classmethod:
#     A class method is a method that receives the class itself as the first argument, conventionally named cls. 
#     It can access and modify class-level data and is often used to define factory methods. 
#     A factory method is a method that creates and returns an object of the class. 
#     It acts as an alternative constructor, allowing objects to be created in different ways.

# class C:
#     @classmethod
#     def method(cls, arg1, arg2, ...):
#         pass

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

p = Person.from_birth_year("Jake", 2000)
print(p.name)       # Jake
print(p.age)        # 26

# @classmethod allows from_birth_year() to receive cls and cls(name, age) creates a new object of the class.