# Define functions
def cross_bridge(steps):
  for step in range(steps):
    print("Crossed step.")

  if (steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

def run():
  print("Please tell me how many steps over the bridge to take:")
  steps = int(input())
  cross_bridge(steps)

# Call function

#run()
