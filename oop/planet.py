from human import Human 
from robot import Robot

# Define Planet class
class Planet:
  # Instance variables
  def __init__(self):
    self.inhabitants = {
    "humans": [],
    "robots": []
    }

  # Instance method for adding a human 
  def add_human(self, human):
    self.inhabitants["humans"].append(human)

  # Instance method for removing a human 
  def remove_human(self, human):
    self.inhabitants["humans"].remove(human)

  # Instance method for adding a robot 
  def add_robot(self, robot):
    self.inhabitants["robots"].append(robot)

  # Instance method for removing a robot
  def remove_robot(self, robot):
    self.inhabitants["robots"].remove(robot)

# Magic methods for displaying data
  def __repr__(self):
    return "humans = {}, robots = {}".format(self.inhabitants["humans"], self.inhabitants["robots"])

  def __str__(self):
    if len(self.inhabitants["humans"]) > 0 and len(self.inhabitants["robots"]) > 0:
      return "The {} humans on this planet.\nThe are {} robots on this planet".format(len(self.inhabitants["humans"]), len(self.inhabitants["robots"]))
    elif len(self.inhabitants["humans"]) == 0 and len(self.inhabitants["robots"]) > 0:
      return "There are no humans on this planet.\nThe are {} robots on this planet.".format(len(self.inhabitants["robots"]))
    elif len(self.inhabitants["humans"]) > 0 and len(self.inhabitants["robots"]) == 0:
      return "The are {} humans on this planet.\nThere are no robots on this planet.".format(len(self.inhabitants["humans"]))
    else:
      return "This planet is empty!"

# Testing area
if (__name__ == "__main__"):
  planet = Planet()
  print(planet)

  darren = Human("Darren")
  beep = Robot("Beep")
  bop = Robot("Bop")
  bender = Robot("Bender")

  planet.add_human(darren)
  print(planet)
  planet.add_robot(beep)
  print(planet)

  planet.add_robot(bop)
  planet.add_robot(bender)
  print(planet)

  planet.remove_robot(bender)
  planet.remove_human(darren)
  print(planet)
  
