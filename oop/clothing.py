
class Clothing:
  def __init__(self, colour, material, size):
    self.colour = colour
    self.material = material
    self.size = size
  
  def __str__(self):
    return f"This piece of clothing is {self.colour}, the material is {self.material} and the size is {self.size}"
  
  def __repr__(self):
    return f"clothing colour = {self.colour}, clothing material = {self.material}, clothing size = {self.size}"