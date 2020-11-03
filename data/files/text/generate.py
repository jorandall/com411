# Define the search function
import csv

def search(file_name):
  print("Searching...", end="")
  data = {}

  with open(file_name) as csvfile:
    for line in csvfile:
      if line.startswith("Section"):
        section = line.split(":")
      else:
        data.append({section: line[:-1]})
  
  print("Done!")
  return data



# Define the run function and write the new document
def run():
  data = search("data/files/text/books.txt")
  csv.write("data/files/text/generated.csv", data)

run()