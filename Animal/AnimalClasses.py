# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animal:

    def __init__(self,Name,Age):
        self.name = Name
        self.age = Age

    def move(self):
        print(self.name + " is moving")

    def eat(self):
        print(self.name + " is eating")

class Dog(Animal):
    pass

class Fish(Animal):
    pass

class Bird(Animal):
    pass
