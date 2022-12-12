class SpaceObject:
    def __init__(self, name=None):
        self.name = name
    

class Planet(SpaceObject):
    earth = Planet('Earth')

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

class Animal:
    def __init__(self, name=None,
        self.name = name
                 
    def __str__(self):
       return self.name             

class Cat(Animal):
    def __init__(self,):
        self.name = name

class Dog(Animal):
    def __init__(self,):
        self.name = name         


class Chicken(Animal):
    def __init__(self,):
        self.name = name         


print(earth)
