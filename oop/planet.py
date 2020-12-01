# Define Planet class
class Planet:
  # Instance variables
  def __init__(self):
    self.inhabitants = {
    "humans": [],
    "robots": []
    }

  # Instance method for adding a human 
  def add_human(self, name):
    self.inhabitants["humans"].append(name)

  # Instance method for removing a human 
  def remove_human(self, name):
    self.inhabitants["humans"].remove(name)

  # Instance method for adding a robot 
  def add_robot(self, name):
    self.inhabitants["robots"].append(name)

  # Instance method for removing a robot
  def remove_robot(self, name):
    self.inhabitants["robots"].remove(name)

# Magic methods for displaying data
  def __repr__(self):
    return "humans = {}, robots = {}".format(self.inhabitants["humans"], self.inhabitants["robots"])

  def __str__(self):
    if len(self.inhabitants["humans"]) > 0 and len(self.inhabitants["robots"]) > 0:
      return "The humans on this planet are {}.\nThe robots on this planet are {}".format(str(self.inhabitants["humans"])[1:-1].replace("'",""), str(self.inhabitants["robots"])[1:-1].replace("'", ""))
    elif len(self.inhabitants["humans"]) == 0 and len(self.inhabitants["robots"]) > 0:
      return "There are no humans on this planet.\nThe robots on this planet are {}".format(str(self.inhabitants["robots"])[1:-1].replace("'", ""))
    elif len(self.inhabitants["humans"]) > 0 and len(self.inhabitants["robots"]) == 0:
      return "The humans on this planet are {}.\nThere are no robots on this planet.".format(str(self.inhabitants["humans"])[1:-1].replace("'",""))
    else:
      return "This planet is empty!"

# Testing area
planet = Planet()
print(planet)
planet.add_human("Darren")
print(planet)
planet.add_robot("Beep")
print(planet)

planet.add_robot("Bop")
planet.add_robot("Bender")
print(planet)

planet.remove_robot("Bender")
planet.remove_human("Darren")
print(planet)
  
