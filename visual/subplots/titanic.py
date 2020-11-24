import matplotlib.pyplot as plt
import csv

def read_data():
  # Dictionary for our data
  data = {
      "survived": [],
      "sex": [],
      "age": [],
      "fare": []
  }

# Open CSV file
  with open("visual/subplots/titanic.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
# Specify the headers and confirm which headers we want to use
    header = next(csv_reader)   # Define header and tell program to read next line
    

# Read in the data from the CSV file and append to the dictionary accordingly
    for line in csv_reader:
      survived = line[1].strip()
      sex = line[4].strip()
      age = line[5].strip()
      fare = line[9].strip()
      
      if (survived != "" and sex != "" and age != "" and fare != ""):
        data["survived"].append(bool(int("survived")))

        if (int(sex) == 0):
          data["sex"].append("male")
        else:
          data["sex"].append("female")
        
        data["age"].append(float(age))
        data["fare"].append(round(float(fare), 2))

# Return completed dictionary
  return data

def plot_age_vs_survival(ax, data):
  # Create dictionaries for each age group
  children = {"survived": [], "deceased": []}
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

  ax.scatter(range(len(survived)), survived, labels="Survived")
  ax.scatter(range(len(survived)), deceased, labels="Deceased")
  ax.set_ylabel("fare")
  ax.legend()
  ax.set_title("Fare vs Survival")

def plot_sex_vs_survival(ax, data):
  males = {"survived": [], "deceased": []}
  females = {"survived": [], "deceased": []}

  for index in range(len(data["sex"])):
    sex = data["sex"][index]
    if (sex == "male" and data["survived"][index]):
      males["survived"].append(sex)
    elif (sex == "male" and not data["survived"][index]):
      males["deceased"].append(sex)
    elif (sex == "female" and data["survived"][index]):
      females["survived"].append(sex)
    else:
      females["deceased"].append(sex)
  
  labels = ["male", "female"]
  survivors = [len(males["survived"]), len(females["survived"])]
  deceased = [len(males["deceased"]), len(females["deceased"])]

  ax.bar(labels, survivors, label="Survived")
  ax.bar(labels, deceased, bottom=survivors, label="Deceased")
  ax.set_ylabel("Passengers")
  ax.legend()
  ax.set_title("Sex vs Survival")

def plot_all_vs_survival(ax, data):
  children = {
    "male": {"survived": [], "deceased": []},
    "female": {"survived": [], "deceased": []}
  }

  adults = {
    "male": {"survived": [], "deceased": []},
    "female": {"survived": [], "deceased": []}
  }

  elderly = {
    "male": {"survived": [], "deceased": []},
    "female": {"survived": [], "deceased": []}
  }

  for index in range(len(data["age"])):
    age = data["age"][index]

    # children
    if (age < 18):
      if (data["sex"][index] == "male" and data["survived"][index]):
        children["male"]["survived"].append(age)
      elif (data["sex"][index] == "male" and not data["survived"][index]):
        children["male"]["deceased"].append(age)
      elif (data["sex"][index] == "female" and data["survived"][index]):
        children["female"]["survived"].append(age)
      elif (data["sex"][index] == "female" and not data["survived"][index]):
        children["female"]["survived"].append(age)

    # adults
    elif (age < 65):
      if (data["sex"][index] == "male" and data["survived"][index]):
        adults["male"]["survived"].append(age)
      elif (data["sex"][index] == "male" and not data["survived"][index]):
        adults["male"]["deceased"].append(age)
      elif (data["sex"][index] == "female" and data["survived"][index]):
        adults["female"]["survived"].append(age)
      elif (data["sex"][index] == "female" and not data["survived"][index]):
        adults["female"]["survived"].append(age)

    # elderly
    else:
      if (data["sex"][index] == "male" and data["survived"][index]):
        elderly["male"]["survived"].append(age)
      elif (data["sex"][index] == "male" and not data["survived"][index]):
        elderly["male"]["deceased"].append(age)
      elif (data["sex"][index] == "female" and data["survived"][index]):
        elderly["female"]["survived"].append(age)
      elif (data["sex"][index] == "female" and not data["survived"][index]):
        elderly["female"]["survived"].append(age)
  
  x_labels = ["children", "adults", "elderly"]
  male_survivors = [len(children["male"]["survived"]), len(adults["male"]["survived"]), len(elderly["male"]["survived"])]
  female_survivors = [len(children["female"]["survived"]), len(adults["female"]["survived"]), len(elderly["female"]["survived"])]

  ax.plot(x_labels, male_survivors, label="Male Survivors")
  ax.plot(x_labels, female_survivors, label="Female Survivors")
  ax.set_title("Age, Sex vs Survival")
  ax.legend()
  ax.set_title("Fare vs Survival")


# Define run function
def run():
  data = read_data()
# Specify how many subplots and the title 
  fig, axs = plt.subplots(2, 2)
  
  # Display plots
  plot_age_vs_survival(axs[0, 0], data)
  plot_fare_vs_survival(axs[0, 1], data)
  plot_sex_vs_survival(axs[1, 0], data)
  plot_all_vs_survival(axs[1, 1], data)

  plt.tight_layout()
  plt.show()
      
run()