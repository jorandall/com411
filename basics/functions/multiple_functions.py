# Define ladder function
def display_ladder(steps):
  steps_taken = 0
  while steps_taken < steps:
    print("| |")
    print(" *** ")
    steps_taken += 1
  print("| |")

# Define create ladder function
def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)

# Call function
create_ladder()