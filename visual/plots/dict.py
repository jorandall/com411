import matplotlib.pyplot as plt

def data():
  paths = {}
  print("What type of line would you like (dotted, dashed or solid)?")
  line = input()
  print("What colour would you like (red, green or blue)?")
  colour = input()
  print("What style of marker would you like (circle, square or triangle?")
  shape = input()
  
  if line == "dotted":
    paths[line] = ":"
  elif line == "dashed":
    paths[line] = "--"
  elif line == "solid":
    paths[line] = "-"
    
  if colour == "red":
    paths[colour] = "r"
  elif colour == "green":
    paths[colour] = "g"
  elif colour == "blue":
    paths[colour] = "b"
    
  if shape == "circle":
    paths[shape] = "o"
  elif shape == "square":
    paths[shape] = "s"
  elif shape == "triangle":
    paths[shape] = "^"
  
  return paths
  
def generate():
  print("How many lines would you like to display?")
  lines = input()
  
  for line in lines:
    data_dict = data()
    plt.plot(line, data_dict[1])
    plt.show()
  
def run():
  print("Running...")
  generate()
  print("Done!")
  
run()
    
    
    
    