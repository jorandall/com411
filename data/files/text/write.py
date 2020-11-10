# Define the search function
def search(file_name):
  print("Searching...", end="")
  sections = []
  books = []

  with open(file_name) as file:
    for line in file:
      if line.startswith("Section"):  # If the line starts with section
        section_name = line.split(":") # split the string after the colon
        sections.append(section_name[1][:-1]) # -1 removing \n from output
      else:
        books.append(line[:-1]) # -1 removing \n from output
  
  print("Done!")
  return(sections, books)

# Define the save function
def save(file_name, library):
  print("Saving...", end="")

  with open(file_name, "w") as file:
    
    file.write("Sections: ")
    for index in range(len(library[0])):
      if (index < len(library[0]) -1):
        file.write(f"{library[0][index]}, ")
      else:
        file.write(f"{library[0][index]}.")

    file.write(f"\nBooks: ")
    for index in range(len(library[1])):
      if (index < len(library[1]) - 1):
        file.write(f"{library[1][index]}, ")
      else:
        file.write(f"{library[1][index]}.")

  print("Done!")

# Define the run function and write the new document
def run():
  data = search("data/files/text/books.txt")
  save("data/files/text/section-books.txt", data)

run()