# Define function for retrieving directions
def directions():
  directions = ["Move Forward", 
                "Move Backward", 
                "Turn Left", 
                "Turn Right"]
  
  return directions

# Define function to choose a direction
def menu():
  print("Please select a direction:")
  direction = directions()

  for index in range(len(direction)):
    print("{}: {}".format(index, direction[index]))

  # Ask the user to choose an index number
  index_choice = int(input())

  return direction[index_choice]


# Define function to run the program
def run():
  route = []

  print("Working out escape route...\n")

  for count in range(5):
    direction = menu()
    route.append(direction)
  
  print("\nEscape route: {}".format(route))

# Run function call
#run()
