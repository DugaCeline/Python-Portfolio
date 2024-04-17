# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The methods should be specific for the animal, and the general animal should not be able to use 
move() or eat() method. (Study abstraction)
The methods don't need to do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.


"""
# Your Code Below:

class Animal:

    def __init__(self,Name,Age):
        self.name = Name
        self.age = Age

    def move(self):
        raise NotImplementedError("Child class should be implementing move method")

    def eat(self):
        raise NotImplementedError("Child class should be implementing eat method")

class Dog(Animal):

    def eat(self):
        print(self.name + " is eating bones")

    def move(self):
        print(self.name + " is running")

class Fish(Animal):

    def eat(self):
        print(self.name + " is eating seaweed")

    def move(self):
        print(self.name + " is swimming")

class Bird(Animal):

    def eat(self):
        print(self.name + " is eating seeds")

    def move(self):
        print(self.name + " is flying")
