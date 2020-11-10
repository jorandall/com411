import matplotlib.pyplot as plt

# Define function to coordinate 
def coordinate():
  print("Please enter the value for 'X':")
  x = int(input())
  print("Please enter the value for 'Y':")
  y = int(input())
  return (x, y)

# Define function to work out the path
def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  
  for count in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  
  return [x_values, y_values]
  
# Define function to run the progra,
def run():
  values = path()
  plt.plot(values[0], values[1], 'r--o')
  plt.xlabel("x values")
  plt.ylabel("y labels")
  plt.show()
  
run()