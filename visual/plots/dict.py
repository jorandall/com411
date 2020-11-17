import matplotlib.pyplot as plt
import random as rnd

# Define the data function to ask user how lines should be displayed
def data():
  paths = {}

  # Ask user for line details
  print("What type of line would you like (:, -- or -)?")
  line_style = input()
  print("What colour would you like (r, g or b)?")
  colour = input()
  print("What style of marker would you like (o, s or ^?")
  marker_style = input()

  # Update dictionary with user responses
  paths["line_style"] = line_style
  paths["colour"] = colour
  paths["marker_style"] = marker_style
  
  return paths

# Define the generate function to ask user for how many lines
def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  
  for num_line in range(num_lines):
    values = data()
    x = [0, rnd.randrange(1, 10)]
    y = [0, rnd.randrange(1, 10)]
    plt.plot(x, y, "{}{}{}".format(values["line_style"], values["colour"], values["marker_style"]))

  plt.show()

# Define run function
def run():
  print("Running...")
  generate()

  print("Done!")

# Function call for run
run()
    
    
    
    