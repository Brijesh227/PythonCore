# Abstract base class:
#   - Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. 
#   - Abstract classes cannot be instantiated directly.(TypeError)
#   - serves as a blueprint for other classes.

#   - Abstract classes are created using abc module and @abstractmethod decorator, 
#   allowing developers to enforce method implementation in subclasses while hiding complex internal logic.

# Components of Abstraction
# 1. Abstract Method
# 2. Concrete Method  
# 3. Abstract Properties
# 4. Abstract Class Instantiation

# for internal working refer: https://chatgpt.com/share/6a27a48d-9bbc-8324-b5d5-15a8495b0b4a
# It's "a method that subclasses are required to provide before objects can be created.


from abc import ABC, abstractmethod

class Greet(ABC):

    @property
    @abstractmethod         # Abstract property, must be implemented by subclasses
    def greet(self):
        pass

    @abstractmethod
    def say_hello(self):    # Abstract method
        pass

    def greeting():         # Concrete Method
        print("Namaste")

class English(Greet):
    @property
    def greet(self):
        return "hi"

    def say_hello(self):
        return "Hello!"

g = English()
print(g.greet)          # hi
print(g.say_hello())    # Hello!

# but still valid to add implementation in abstractmethod, but sub class must still implementation of abstractmethod
# same applies for abstract properties

from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

payment = PaymentGateway()   # ❌ TypeError

class Stripe(PaymentGateway):

    def pay(self, amount):
        super().pay(amount)
        print("Stripe processing")


# A Deeper Mental Model

# Think of abstraction as two separate concepts:

# 1. Contract (mandatory)
# @abstractmethod
# def pay(self):
#     ...

# Means:

# Every subclass MUST provide this method.

# 2. Shared implementation (optional)
# @abstractmethod
# def pay(self):
#     print("validation")

# Means:
# Every subclass MUST provide this method, but here is some reusable logic if you want it.