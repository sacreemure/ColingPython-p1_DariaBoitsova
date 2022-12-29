class SpaceObject:
    def __init__(self, name=None):
        self.name = name


class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or 0

    def __str__(self):
        return f'Population of {self.name} = {self.population}'


class Animal:
    def __init__(self, name=None, planet=None):
        self.name = name
        self.planet = planet

    def creation(self, planet):
        self.planet = planet
        self.planet.population += 1


class Dog(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.food = 15

    def eat(self):
        self.food += 5

    def play(self):
        self.food -= 5


class Cat(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.food = 20

    def eat(self):
        self.food += 15

    def play(self):
        self.food -= 5


class Chicken(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.food = 30
        

    def eat(self):
        self.food += 20
        

    def play(self):
        self.food -= 5


earth = Planet('Earth')

dogs = [Dog('Druzhok', earth),
        Dog('Belka', earth),
        Dog('Bobik', earth),
        ]
cats = [Cat('Musya', earth)]
chickens = [Chicken('Valya', earth),
            Chicken('Katya', earth)
            ]

print(earth)
