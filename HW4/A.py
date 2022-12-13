from space import SpaceObject

class Planet (SpaceObject):
    def __init__(self, name):
        super().__init__(name)
        self.population = 0

    def __str__(self):
        return f'We have {self.population} creatures on {self.name}!'


    def add(self, other):
        self.population += 1

    
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.legs = 4
        self.has_horns = True
        self.is_carnivorous = False

    def moo(self):
        print(f'{self.name} says Moo!')


class Wolf(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.legs = 4
        self.has_horns = False
        self.is_carnivorous = True

    def woof(self):
        print(f'{self.name} says Woof!')

class Python(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.legs = 0
        self.has_horns = False
        self.is_carnivorous = True

    def crawl(self, dest='str'):
        print(f'{self.name} crawls to {dest}!')


Dave = Python('Dave')
Stacey = Cow('Stacey')
Jeff = Wolf('Jeff')

Earth = Planet('Earth')
Earth.add(Dave)
Earth.add(Stacey)
Earth.add(Jeff)

print(Earth)