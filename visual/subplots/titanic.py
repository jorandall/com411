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
        data["survived"].append(bool(int("Survived")))

        if (int(Sex) == 0):
          data["sex"].append("male")
        else:
          data["sex"].append("female")
        
        data["age"].append(float(age))
        data["fare"].append(round(float(fare), 2))

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
    if (age < 18 and data["survived"][index]):
      children["survived"].append(age)
    elif (age < 18 and not data["survived"][index]):
      children["deceased"].append(age)
    elif (age < 65 and data["survived"][index]):
      adults["survived"].append(age)
    elif (age < 65 and not data["survived"][index]):
      adults["deceased"].append(age)
    elif (data["survived"][index]):
      elderly["survived"].append(age)
    else:
      elderly["deceased"].append(age)

  # Prepare labels and totals
  labels = ["children", "adults", "elderly"]
  survivors = [len(children["survived"]), len(adults["survived"]), len(elderly["survived"])]
  deceased = [len(children["deceased"]), len(adults["deceased"]), len(elderly["deceased"])]

  # Display suitable bar plots
  ax.bar(labels, survivors, label="Survived")
  ax.bar(labels, deceased, bottom=survivors, label ="Deceased")
  ax.set_ylabel("age")
  ax.legend()
  ax.set_title("Age vs Surivival")

def plot_fare_vs_survival(ax, data):
  survived = []
  deceased = []

  for index in range (len(data["fare"])):
    fare = data["fare"][index]
    if (data["survived"][index]):
      survived.append(data["fare"][index])
    else:
      deceased.append(data["fare"][index])



# Define run function
def run():
  data = read_data()
# Specify how many subplots and the title 
  fig, axs = plt.subplots(2, 2)
  fig.suptitle("Titanic Statistics")



  plt.tight_layout()
  plt.show()
      
run()