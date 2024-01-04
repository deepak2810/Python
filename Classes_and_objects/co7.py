# classe and object demo examples.

class Student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print(" Hi I am ", self.name +
              " Student of Class X A and i am ", self.age, 'Years old')


Ram = Student('Ram')
Shyam = Student('Shyam')

Ram.speak()
Shyam.speak()
