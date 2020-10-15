# Define function
def climb_ladder(steps_remaining, steps_crossed):
  if steps_remaining > steps_crossed:
    print("Still some way to go!")
  else:
    print("We are almost there!")

def run():
  print("How many steps of the ladder remain?")
  steps_remaining = int(input())
  print("How many steps of the ladder have we crossed?")
  steps_crossed = int(input())
  climb_ladder(steps_remaining, steps_crossed)

# Call function
#climb_ladder(5, 2)
#climb_ladder(2, 5)
