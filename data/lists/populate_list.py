# Define function for retrieving directions
def get_directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# Define function to choose a direction

def menu():
  print("Please select a direction")
  directions = get_directions()
  