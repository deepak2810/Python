class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am ", self.name, 'and i am ', self.age, 'years old')


# creating object of the class.

tim = Dog('Tim ', 12)
fred = Dog('Fred ', 3)

tim.speak
