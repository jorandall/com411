import matplotlib.pyplot as plt
import csv

def read_data():
# Open CSV file
  with open("visual/subplots/titanic.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
# Specify the headers and confirm which headers we want to use
    header = next(csv_reader)   # Define header and tell program to read next line
    first_key = header[1].strip() # Survival Rate
    second_key = header[4].strip() # Gender
    third_key = header[5].strip() # Age
    fourth_key = header[9].strip() # Fare
# Dictionary for our data
    data = {
      first_key: [],
      second_key: [],
      third_key: [],
      fourth_key: []
    }
# Read in the data from the CSV file and append to the dictionary accordingly
    for entry in csv_reader:
      survived = entry[1]
      gender = entry[4]
      age = entry[5]
      fare = entry[9]
      
      if (len(survived) == 0) or (len(gender) == 0) or (len(age) == 0) or (len(fare) == 0):
        continue
      else:
        data[first_key].append(int(survived.strip())) 
        data[second_key].append(gender.strip()) 
        data[third_key].append(round(float(age.strip()), 0))
        data[fourth_key].append(round(float(fare), 2)) 

# Return completed dictionary
  return data

# Define run function
def run():
  data = read_data()
# Specify how many subplots and the title 
  fig, axs = plt.subplots(2, 2)
  fig.suptitle("Titanic Statistics")


# Work out the suvivors based on gender
  female_survivors = 0
  male_survivors = 0

  for index in range(len(data["Survived"])):
    if data["Survived"][index] == 1:
      if data["Sex"][index] == "male":
        male_survivors += 1
      elif data["Sex"][index] == "female":
        female_survivors += 1

  # Work out fare based on survivors
  survivors_fare = []
  non_survivors_fare = []

  for index in range(len(data["Survived"])):
    if data["Survived"][index] == 1:
      survivors_fare.append(data["Fare"][index])
    else:
      non_survivors_fare.append(data["Fare"][index])
  
  # Work out survivors age ranges:
  sixteen_and_under = []
  seventeen_to_twentyfour = []
  twentyfive_to_thirtyfour = []
  thirtyfive_to_fortyfour = []
  fourtyfive_to_fiftyfour = []
  fiftyfive_plus = []

  for index in range(len(data["Survived"])):
    if data["Survived"][index] == 1:
      if data["Age"][index] <= 16:
        sixteen_and_under.append(data["Age"][index])
      elif data["Age"][index] > 16 and data["Age"][index] <= 24:
        seventeen_to_twentyfour.append(data["Age"][index])
      elif data["Age"][index] > 24 and data["Age"][index] <= 34:
        twentyfive_to_thirtyfour.append(data["Age"][index])
      elif data["Age"][index] > 34 and data["Age"][index] <= 44:
        thirtyfive_to_fortyfour.append(data["Age"][index])
      elif data["Age"][index] > 44 and data["Age"][index] <= 54:
        fourtyfive_to_fiftyfour.append(data["Age"][index])
      elif data["Age"][index] > 54:
        fiftyfive_plus.append(data["Age"][index])

  


# First subplot - pie chart showing gender percentage rates for survival
  axs[0,0].set_title(
    "Survival Rate By Gender", # Subplot title name
    size=10 # Subplot title size
    )
  axs[0,0].pie(
    (female_survivors, male_survivors), # Data for the subplot
    labels=(f"Female ({female_survivors})", f"Male ({male_survivors})"), # Subplots labels
    textprops={"fontsize": 8}, # Labels size
    autopct=("%1.1f%%") # Show percentage in pie chart
    ) 
  
# Second subplot
  axs[0,1].set_title(
    "Survival Rate by Fare Paid", # Subplot title name
    size=10 # Subplot title size
    )

  axs[0,1].plot(survivors_fare, "r", label="Survivors")
  axs[0,1].plot(non_survivors_fare,  "b", label="Non-Survivors")
  axs[0,1].legend(loc="upper right", prop={"size": 6})

  # Third subplot
  axs[1,0].set_title(
    "Survival Rate by Age Groups", # Subplot title name
    size=10 # Subplot title size
    )
  axs[1,0].pie(
    (len(sixteen_and_under), 
    len(seventeen_to_twentyfour), 
    len(twentyfive_to_thirtyfour), 
    len(thirtyfive_to_fortyfour),
    len(fourtyfive_to_fiftyfour),
    len(fiftyfive_plus)
    ),
    # Subplots labels
    labels=("<17", "17-24", "25-34", "35-44", "45-54", "55+"), 
    textprops={"fontsize": 8}, # Labels size
    autopct=("%1.1f%%")
  )






  plt.tight_layout()
  plt.show()
      
run()