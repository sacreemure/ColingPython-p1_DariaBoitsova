class SpaceObject:
    def __init__(self, name=None):
        self.name = name
    

class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or []
    
    def __str__(self):
        return f'Population of {self.name} = {self.population}


class Animal:
    def __init__(self, name=None, color=None, food=10)
        self.name = name
        self.color = color
        self.food = food
         
    def __str__(self):
       return self.name

    def add(self):
        self.population += 1
    
    def feed(self):
        self.food += 1
        return "I'm full"

    
class Cat(Animal):
    def __init__(self, name=None, color=None, food=2):
        self.name = name
        self.color = color
        self.food = food
        
    
    def sound(self):
        return f'{self.name}: мяу!'

    
class Dog(Animal):
    def __init__(self, name=None, color=None, food=5):
        self.name = name
        self.color = color
        self.food = food
        
       
    def bark(self):
        return f'{self.name}: гав гав'


class Chicken(Animal):
    def __init__(self, name=None, color=None, food=1):
        self.name = name
        self.color = color
        self.food = food
        
    
    def cluck(self):
        return f'{self.name}: ко ко ко'

 

earth = Planet('Earth')

cats = [Cat('Musya', 'white'), Cat('Vasya', 'black')]
dogs = [Dog('Bobik', 'brown')]
chickens = [Chicken('Valya', 'yellow'), Chicken('Katya', 'grey')]

print(earth)

