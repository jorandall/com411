import random as rnd
from planet import Planet


class Universe:
  def __init__(self):
    self.planets = []
  
  def generate(self, new_planet, inhabitants=Planet.inhabitants):
    new_planet = Planet

    for iterations in range(5):
      humans = [0, rnd.randrange(1, 100)]
      robots = [0, rnd.randrange(1, 100)]

    new_planet.add_human(self, humans)
    new_planet.add_robot(self, robots)

    self.planets.append(new_planet)

  def __str__(self):
    return f"The planets in this universe are {self.planets}"


universe = Universe()
universe.generate("Mars")
print(universe)