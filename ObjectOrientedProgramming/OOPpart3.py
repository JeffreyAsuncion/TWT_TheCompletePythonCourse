# Inheritance

class Dog(object):
    def __init__(self, name, age):
        self.name = name    # attributes
        self.age = age      # attributes

    def speak(self): # Methods
        print("Woof Woof, I am ", self.name, ' and I am ', self.age, ' years old.')

    def talk(self):
        print("Bark!")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color    # attributes

    def talk(self):
        print("Meow!") # overload / override methods


jim = Dog("Jim", 70)
jim.talk()

tim = Cat("Tim", 5, "purple")
tim.talk()
