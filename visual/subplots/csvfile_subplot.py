import matplotlib.pyplot as plt
import csv

# Read in the file and store in the correct dictionary entry
def read_data():
  with open("visual/subplots/temps.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    data = {"week 1": [],
            "week 2": []
            }
    
    for row in csv_reader:
      data["week 1"].append(int(row[0].strip()))
      data["week 2"].append(int(row[1].strip()))    
    
  return data

# Plot the graph and display results
def run():
  data = read_data()
  fig, axs = plt.subplots(2, 1, sharex="all")

  axs[0].plot(data["week 1"])
  axs[1].plot(data["week 2"])
  plt.show()
      
run()