from tech import Tech

class Laser(Tech):
  def __init__(self):
    self.MAX_RANGE = 100
  
  def activate(self):
    print("Laser activated!")

  def fire(self):
    print("Laser fired!")

  def deactivate(self):
    print("Laser deactivated!")