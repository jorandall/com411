from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

import random

class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."

  def generate(self):
    # create a new planet
    planet = Planet()

    # populate with random humans and robots
    for index in range(random.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_inhabitant(robot)

    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add_inhabitant(human)

    # add to list of planets
    self.planets.append(planet)

  def show_populations(self):
    num_humans = 0
    num_robots = 0

    for planet in self.planets:
      for inhabitant in planet.inhabitants:
        if isinstance(inhabitant, Human):
          num_humans += 1
        elif isinstance(inhabitant, Robot):
          num_robots += 1
    
      print(f"Found {num_humans} humans.")
      print(f"Found {num_robots} robots.")

    num_subplots = len(self.planets)
    
    fig, axs = plt.subplots(1, num_subplots)
    
    for index in range(num_subplots):

      if (num_subplots == 1):
        axs.bar([1, 2], [num_humans, num_robots])
      else:
        axs[index].bar([1, 2], [num_humans, num_robots])

    plt.tight_layout()  
    plt.show()


if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.generate()
  universe.show_populations()