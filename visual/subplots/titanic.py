import matplotlib.pyplot as plt
import csv

def read_data():
  # Dictionary for our data
    data = {
      "Survived": [],
      "Sex": [],
      "Age": [],
      "Fare": []
    }

# Open CSV file
  with open("visual/subplots/titanic.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
# Specify the headers and confirm which headers we want to use
    header = next(csv_reader)   # Define header and tell program to read next line
    

# Read in the data from the CSV file and append to the dictionary accordingly
    for line in csv_reader:
      survived = line[1].strip()
      gender = line[4].strip()
      age = line[5].strip()
      fare = line[9].strip()
      
      if (survived != "" and sex! = "" and age !="" and fare !=""):
        data["Survived"].append(bool(int("Survived")))

        if (int(Sex) == 0):
          data["Sex"].append("male")
        else:
          data["Sex"].append("female")
        
        data["Age"].append(float(age))
        data["Fare"].append(round(float(fare), 2))

# Return completed dictionary
  return data

def plot_age_vs_survival(ax, data):
  # Create dictionaries for each age group
  childen = {"survived": [], "deceased": []}
  adults = {"survived": [], "deceased": []}
  elderly = {"survived": [], "deceased": []}

  # Populate each dictionary
  for index in range (len(data["Age"])):
    age = data["Age"][index]

# Define run function
def run():
  data = read_data()
# Specify how many subplots and the title 
  fig, axs = plt.subplots(2, 2)
  fig.suptitle("Titanic Statistics")



  plt.tight_layout()
  plt.show()
      
run()