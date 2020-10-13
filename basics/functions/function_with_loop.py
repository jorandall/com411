# Define function
def cross_bridge(distance):
  step = 0
  while step != distance:
    print("Crossed step")
    step += 1
  if distance > 5:
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")


cross_bridge(3)
cross_bridge(6)