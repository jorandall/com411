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
        data["Survived"].append(row[1].strip())
        data["Sex"].append(row[4].strip())
        data["Age"].append(int(0, row[5].strip()))
        data["Fare"].append(float(0, round(row[9], 2).strip()))

  return data

print(read_data())