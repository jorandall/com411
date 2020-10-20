# Define function for getting directions
def get_directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# Define function for showing index for each direction
def menu():
  print("Please select a direction:")
  direction = get_directions()

  for index in range(len(direction)):
    print("{} : {}.".format(index, direction[index]))

# Define function to run program
def run():
  print(menu())

# Run function call
run()