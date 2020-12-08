from inhabitant import Inhabitant

# Define Human class
class Human(Inhabitant):
  
  # Initialiser
  def __init__(self, name="Human"):
    super().__init__(name)

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

  # Human object
  human = Human()
  human.display()
  print(human)
  print(repr(human))

  human.grow()
  human.move(30)
  print(human)
  human.grow()
  human.eat(10)
  print(human)
  human.eat(50)
  human.move(100)
