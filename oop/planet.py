# Define Planet class
class Planet:
  # Instance variables
  humans = []
  robots = []

  # Instance method for adding a human 
  def add_human(self, name):
    Planet.humans.append(name)

  # Instance method for removing a human 
  def remove_human(self, name):
    Planet.humans.remove(name)

  # Instance method for adding a robot 
  def add_robot(self, name):
    Planet.robots.append(name)

  # Instance method for removing a robot
  def remove_robot(self, name):
    Planet.robots.remove(name)

# Magic methods fo
  def __repr__(self):
    return f"humans = {Planet.humans}, robots = {Planet.robots}"

  def __str__(self):
    return f"The humans on this planet are {Planet.humans}.\nThe robots on this planet are {Planet.robots}"

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
  
