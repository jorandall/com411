import matplotlib.pyplot as plt

# Read in the data file,  store data in a list and return completed list
def read_data(file_name):
  temperatures = []

  with open(file_name) as file:
    for line in file:
      temperature = float(line.strip())
      temperatures.append(temperature)
  
  return temperatures

# Define the run function 
def run():
  data = read_data("visual/subplots/temps.txt")
  fig, (ax1, ax2) = plt.subplots(1, 2)

# Display a line graph
  ax1.plot(range(1, 8), data)
# Display a bar graph
  ax2.bar(range(1,8), data)

  plt.tight_layout()
  plt.show()

run()