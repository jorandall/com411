# Define movements function
def movements():
  path = ["Move Forward", 
          10, 
          "Move Backward", 
          5, 
          "Move Left", 
          3, 
          "Move Right", 
          1]
          
  return path

# Define run function
def run():
  print("Moving...")
  path = movements()

  # Loop for working through the list and pairing up 2 indexes
  for index in range (0, len(path), 2):
    print("{} for {} steps.".format(path[index], path[index+1]))
  
# Run function call
run()
  