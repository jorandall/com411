from tech import Tech

class Jetpack(Tech):
  MAX_RANGE = 100

  def __init__(self):
    super().__init__()
    
  def activate(self):
    print("Jetpack activated!")

  def fly(self, distance):
    if distance > Jetpack.MAX_RANGE:
      print(f"Jetpack flown to max range {Jetpack.MAX_RANGE}")
    else:
      print(f"Flying with jetpack {distance}!")

  def deactivate(self):
    print("Jetpack deactivated!")

  def __str__(self):
    return f"The jetpack has a max range of {Jetpack.MAX_RANGE}"
  
  def __repr__(self):
    return f"Jetpack max range = {Jetpack.MAX_RANGE}"