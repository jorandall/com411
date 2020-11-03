# Define the search function
def search(file_name):
  print("Searching...", end="")
  sections = []
  books = []

  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):
        split = line.split(":")
        sections.append(split[1][:-1])
      else:
        books.append(line[:-1])
  
  print("Done!")
  return(sections, books)

# Define the save function
def save(file_name, library):
  print("Saving...", end="")

  with open(file_name, "w") as file:
    file.write(f"Sections: {library[0]}")
    file.write(f"\nBooks: {library[1]}")

  print("Done!")

# Define the run function
def run():
  data = search("data/files/text/books.txt")
  save("data/files/text/section-books.txt", data)

run()