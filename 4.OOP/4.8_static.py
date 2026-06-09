# Static Method
#   Static method is a method defined inside a class that does not depend on any instance or class data.
#   A static method is a method that does not receive self or cls automatically. 
#   It cannot access or modify class or instance data directly unless explicitly passed.
#   Typically used to define utility functions that logically belong to the class but do not depend on class or instance data.

# class C:
#     @staticmethod
#     def method(arg1, arg2, ...):
#         pass

class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(20))
p = Person(16)
print(p.is_adult(p.age))