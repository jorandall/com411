# Define the search function
def search(file):
  print("Searching...")
  with open(file) as file:
    for line in file:
      print(f"Looked in {line}", end ="")
  print("\n...Done!")

def run():
  search("data/files/text/locations.txt")

run()

