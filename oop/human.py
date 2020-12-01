# Define Robot class
class Robot:
  # Class attribute
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100

  def the_laws():
    print(Robot.laws)

  # Initialiser
  def __init__(self):
    # Instance attributes
    self.name = "Robot"
    self.age = 0
    self.energy = Robot.MAX_ENERGY

  # Method to increase age
  def grow(self):
    self.age += 1

  # Method to increase energy
  def eat(self, amount):
    if (self.energy + amount) <= Robot.MAX_ENERGY:
      self.energy = self.energy + amount
    else:
      print("Too full to eat that!")

  # Method to reduce energy due to distance
  def move(self, distance):
    if (self.energy - distance) > 0:
      self.energy = self.energy - distance
    else:
      print("I do not have enough energy to do that.")
  
  # Instance method
  def display(self):
    print(f"I am {self.name}")

  # Debugging method
  def __repr__(self):
    return f"laws={Robot.laws}, name={self.name}, age={self.age}, energy={self.energy}"
  
  # Print method
  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old. My laws are {Robot.laws} and my energy is {self.energy}"


# Define Human class
class Human:
  # Class attribute
  MAX_ENERGY = 100

  # Initialiser
  def __init__(self):
    # Instance attributes
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  # Method to increase age
  def grow(self):
    self.age += 1
  
  # Method to increase energy
  def eat(self, amount):
    if (self.energy + amount) <= Human.MAX_ENERGY:
      self.energy = self.energy + amount
    else:
      print("Too full to eat that!")

  # Method to reduce energy due to distance
  def move(self, distance):
    if (self.energy - distance) > 0:
      self.energy = self.energy - distance
    else:
      print("I do not have enough energy to do that.")

  # Instance method
  def display(self):
    print(f"I am {self.name}")

  # Debugging method
  def __repr__(self):
    return f"name={self.name}, age={self.age}, energy={self.energy}"
  
  # Print method
  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old. My energy level is {self.energy}"

# Testing area
if (__name__ == "__main__"):

  # Robot object
  robot = Robot()
  robot.grow()
  robot.eat(20)
  robot.move(100)
  

  # Human object
  human = Human()
  human.display()
  print(human)
  print(repr(human))