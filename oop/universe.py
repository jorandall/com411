import random as rnd
from planet import Planet


class Universe:
  def __init__(self):
    self.planets = []
  
  def generate(self, new_planet):

    for iterations in range(5):
      humans = rnd.randrange(1, 100)
      new_planet.add_human(humans)
      robots = rnd.randrange(1, 100)
      new_planet.add_robot(robots)

    self.planets.append(new_planet)

  def __str__(self):
    return f"The planets in this universe are {self.planets}"

mars = Planet()
universe = Universe()
universe.generate(mars)
venus = Planet()
universe.generate(venus)
print(universe)