# Static Methods and Class Methods

class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls): # cls is the name of the class
        return len(cls.dogs)

    @staticmethod  # a function grouped with class but does not need class variables or methods
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")

tim = Dog("Tim")
jim = Dog("Jim")


## Class variables
print(Dog.dogs) #call class variable with the Class name without and instance of the class
print(tim.dogs) # is the same as above but using an instance tim

## @staticmethod and @classmethod are called Decorators
## @classmethod
print(Dog.num_dogs())
print(tim.num_dogs()) # this still works but advantage of above saves space
## @static method - do not need the class to be used
print(Dog.bark(5)) # a function grouped with class but does not need class variables or methods
