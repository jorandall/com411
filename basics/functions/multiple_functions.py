# Define ladder function
def display_ladder(steps):

  for step in range(steps):
    print("|  |")
    print("****")

  print("|  |")

# Define create ladder function
def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)

# Call function
#create_ladder()