# Define Planet class
class Planet:
  # Instance variables
  inhabitants = {
  "humans": [],
  "robots": []
  }

  # Instance method for adding a human 
  def add_human(self, name):
    Planet.inhabitants["humans"].append(name)

  # Instance method for removing a human 
  def remove_human(self, name):
    Planet.inhabitants["humans"].remove(name)

  # Instance method for adding a robot 
  def add_robot(self, name):
    Planet.inhabitants["robots"].append(name)

  # Instance method for removing a robot
  def remove_robot(self, name):
    Planet.inhabitants["robots"].remove(name)

# Magic methods for displaying data
  def __repr__(self):
    return "humans = {}, robots = {}".format(Planet.inhabitants["humans"], Planet.inhabitants["robots"])

  def __str__(self):
    return "The humans on this planet are {}\nThe robots on this planet are {}".format(str(Planet.inhabitants["humans"])[1:-1].replace("'",""), str(Planet.inhabitants["robots"])[1:-1].replace("'", ""))

# Testing area
planet = Planet()
planet.add_human("Darren")
planet.add_robot("Beep")
print(planet)

planet.add_robot("Bop")
planet.add_robot("Bender")
print(planet)

planet.remove_robot("Bender")
planet.remove_human("Darren")
print(planet)
  
