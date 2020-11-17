import matplotlib.pyplot as plt
import csv

first_key = None
second_key = None

# Read in the file and store in the correct dictionary entry
def read_data():
  global first_key, second_key

  with open("visual/subplots/temps.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)   # Define header and tell program to read next line
    
    first_key = header[0].strip()
    second_key = header[1].strip()

    data = {
      first_key: [],
      second_key: []
    }
    
    for row in csv_reader:
      data[first_key].append(int(row[0].strip()))
      data[second_key].append(int(row[1].strip()))    

  return data

# Plot the graph and display results
def run():
  data = read_data()
  fig, axs = plt.subplots(2, 1, sharex="all")

  axs[0].plot(data[first_key])
  axs[1].plot(data[second_key])

  plt.tight_layout()
  plt.show()
      
run()