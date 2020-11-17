#import matplotlib.pyplot as plt
import csv

def read_data():
  data ={
    "Survived": [],
    "Sex": [],
    "Age": [],
    "Fare": [],
  }

  with open("visual/subplots/titanic.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      if row != "0":
        data["Survived"].append(int(row[1].strip()))
        data["Sex"].append(str(row[4].strip()))
        data["Age"].append(int(row[5].strip()))
        data["Fare"].append(float(round(row[9], 2).strip()))

  return data

print(read_data())