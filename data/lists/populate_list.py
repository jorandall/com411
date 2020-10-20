# Define function for retrieving directions
def get_directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# Define function to choose a direction
def menu():
  print("Please select a direction:")
  direction = get_directions()

  for index in range(len(direction)):
    print("{} : {}.".format(index, direction[index]))

  choice = int(input())

  return direction[choice]


# Define function to run the program
def run():
  route = []

  print("Working out escape route...\n")

  for i in range(5):
    menu()
    route.append(item)
  
  print("\nEscape route: {}".format(route))

run()