# Creating Classes

class Dog(object):
    def __init__(self, name, age):
        self.name = name    # attributes
        self.age = age      # attributes
        print("Nice you made a dog!")

    def speak(self): # Methods
        print("Woof Woof, I am ", self.name, ' and I am ', self.age, ' years old.')

    def change_age(self, age): # Methods
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

tim = Dog("Tim", 55)
fred = Dog("Fred", 4)

tim.change_age(5)
tim.add_weight(75)
tim.speak()
fred.speak()

print(tim.age)