# a program to illustrate about __init__() Function in python programs.
class Person:
    def __init__(self, name, age):
        self.naem = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age}"


# Creating an object of the person class
person1 = Person("Alice", 30)


# access
