
# Define functions for word chosen by user
def display_box(word):
  num_dashes = 6 + len(word)
  num_spaces = 4 + len(word)
  
  print("-" * num_dashes)
  print("|" + (" " * num_spaces) + "|")
  print("|  {}  |".format(word))
  print("|" + (" " * num_spaces) + "|") 
  print("-" * num_dashes)

def display_lower(word):
  print(word.lower())

def display_upper(word):
  print(word.upper())

def mirrored(word):
  print(word, "| ", end="")
  for position in range(len(word) -1, -1, -1):
    print(word[position], end="")

def repeat(word):
  print("How many times do you want this word repeated?")
  repeat = int(input())
  print(word * repeat)

# Define run function
def run():
  print("Please enter a word:")
  word = input()
  print("""Please choose one of the following options for how to proceed:
  1. Display in a box
  2. Display in lower case
  3. Display in upper case
  4. Display mirrored
  5. Repeat""")
  choice = int(input())

  if choice == 1:
    return display_box(word)
  elif choice == 2:
    return display_lower(word)
  elif choice == 3:
    return display_upper(word)
  elif choice == 4:
    return mirrored(word)
  elif choice == 5:
    return repeat(word)
  else:
    print("{} is not a valid option".format(choice))

# call the run function
run()
