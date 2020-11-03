# Define the search function
import csv

def search(file_name):
  print("Searching...", end="")
  data = {}
  section_name = ""

  with open(file_name) as csvfile:
    for line in csvfile:
      if line.startswith("Section"):
        section = line.split(":")
        section_name = section[1].strip()
      else:
        if (section_name in data):  # Check if already exists, if so add to the end
          values = data[section_name]
          values.append(line.strip())
        else:
          data[section_name] = [line.strip()] # If doesn't exist, add to the beginning
  
  print("Done!")
  return data



# Define the run function and write the new document
def run():
  data = search("data/files/text/books.txt")

  with open ("data/files/text/generated.csv", "w") as file:

    for item in data.items():
      section = item[0]
      books = item[1]

      for book in books:
        file.write(f"{section}, {book}\n")



run()