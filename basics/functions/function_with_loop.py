# Define function
def cross_bridge(distance):
  for step in range(steps):
    print("Crossed step.")

  if distance > 5:
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

# Call function

cross_bridge(3)
cross_bridge(6)

