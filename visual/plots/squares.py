import matplotlib.pyplot as plt

# Define function to plot small square
def small():
  x = [3, 4, 4, 3, 3]
  y = [3, 3, 4, 4, 3]
  plt.plot(x, y, 'ro:')

# Define function to plot medium square
def medium():
  x = [2, 5, 5, 2, 2]
  y = [2, 2, 5, 5, 2]
  plt.plot(x, y, 'gs--')

# Define function to plot large square
def large():
  x = [1, 6, 6, 1, 1]
  y = [1, 1, 6, 6, 1]
  plt.plot(x, y, 'b-p')

# Define run function
def run():
  small()
  medium() 
  large()
  plt.show()

# Function call to run
run()