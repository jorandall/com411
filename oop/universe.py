import random as rnd
from planet import Planet
from robot import Robot
from human import Human


class Universe:
  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"universe(planets={self.planets}"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."
  
  def generate(self):
    # Create a new planet
    planet = Planet()

    # Populate with random humans and robots
    for index in range(rnd.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)
    
    for index in range(rnd.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add_human(human)

    self.planets.append(planet)



if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.generate()
  print(universe)


