from inhabitant import Inhabitant

# Define Robot class
class Robot(Inhabitant):
  # Class attribute
  laws = "Protect, Obey and Survive"

  def the_laws():
    print(Robot.laws)

  # Initialiser
  def __init__(self, name="Robot"):
    # Instance attributes
    self.name = name
    self.age = 0
    self.energy = Inhabitant.MAX_ENERGY
  
  # Instance method
  def display(self):
    print(f"I am {self.name}")

  # Debugging method
  def __repr__(self):
    return f"robot(laws={Robot.laws}, name={self.name}, age={self.age}, energy={self.energy})"
  
  # Print method
  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old. My laws are {Robot.laws} and my energy is {self.energy}"


# Testing area
if (__name__ == "__main__"):

  # Robot object
  robot = Robot()
  robot.grow()
  robot.eat(20)
  robot.move(15)
  print(repr(robot))