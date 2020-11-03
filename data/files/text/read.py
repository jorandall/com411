# Define the search function
def search(file_name):
  print("Searching...")
  with open(file_name) as file:
    for line in file:
      print(f"Looked in {line[:-1]}.")
  print("...Done!")

# Define the run function
def run():
  search("data/files/text/locations.txt")

# Run function call
run()

