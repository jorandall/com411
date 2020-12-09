from tech import Tech

class Laser(Tech):
  MAX_RANGE = 100
 
  def __init__(self):
    super().__init__()
  
  def activate(self):
    print("Laser activated!")

  def fire(self, range_distance):
    if range_distance > Laser.MAX_RANGE:
      print(f"Fired maximum range of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {range_distance}")

  def deactivate(self):
    print("Laser deactivated!")

  def __str__(self):
    return f"The laser has {Laser.MAX_RANGE} range"
  
  def __repr__(self):
    return f"Laser range = {Laser.MAX_RANGE}"