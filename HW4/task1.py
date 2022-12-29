class SpaceObject:
    def __init__(self, name=None):
        self.name = name
    

class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or 0
    
    def __str__(self):
        return f'Population of {self.name} = {self.population}


class Animal:
    def __init__(self, name=None, planet=None)
        self.name = name
        self.planet = planet
         
    def add(self):
        self.population += 1

    
class Cat(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.food = 5
        
    def feed(self):
        self.food += 1
    
    def sound(self):
        return f'{self.name}: мяу!'

    
class Dog(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.food = 10
        
    def feed(self):
        self.food += 5
        
    def bark(self):
        return f'{self.name}: гав гав'


class Chicken(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.food = 2
        
    def feed(self):
        self.food += 2
        
    def cluck(self):
        return f'{self.name}: ко ко ко'

 

earth = Planet('Earth')

cats = [Cat('Musya', earth), Cat('Vasya', earth)]
dogs = [Dog('Bobik', earth)]
chickens = [Chicken('Valya', earth), Chicken('Katya', earth)]

print(earth)

