import matplotlib.pyplot as plt


def read_data(file_name):
  data = []

  with open(file_name) as file:
    for line in file:
      data.append(line)
  
  return data

# Define the run function 
def run():
  data = read_data("visual/subplots/temps.txt")
  fig, axs = plt.subplots(1, 2)

# Display a line graph
  axs[0].plot(data)
# Display a bar graph
  axs[1].bar(data, data)

  plt.show()

run()