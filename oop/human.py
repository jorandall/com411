# Define Robot class
class Robot:
  # Class attribute
  laws = "Protect, Obey and Survive"

  def the_laws():
    print(Robot.laws)

  # Initialiser
  def __init__(self):
    # Instance attributes
    self.name = "Robot"
    self.age = 0
  
  # Instance method
  def display(self):
    print(f"I am {self.name}")

# Define Human class
class Human:
  # Class attribute
  MAX_ENERGY = 100

  # Initialiser
  def __init__(self):
    # Instance attributes
    self.name = "Human"
    self.age = 0
    self.energy = self.MAX_ENERGY

  # Instance method
  def display(self):
    print(f"I am {self.name}")

# Testing area
if (__name__ == "__main__"):
  robot = Robot()
  robot.display()

if (__name__ == "__main__"):
  human = Human()
  human.display()
