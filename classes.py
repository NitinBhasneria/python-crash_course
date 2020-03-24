# A class is like a blueprint for creating objects. An object has properties and 
#   methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, age):
        self.name = name         #self is this in c++ or php
        self.age = age

    def greeting(self):
        return (f'My name is {self.name} and I am {self.age}')

    def has_birthday(self):
        self.age += 1

# Extend class
class Customer(User):     # child class customer parent class user
    # Constructor
    def __init__(self, name, age):
        self.name = name         #self is this in c++ or php
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    
# Init user object
brad = User('Nitin Bhasneria', 20)
# Init customer
janet =  Customer('Janet Johnson', 26)
janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())
