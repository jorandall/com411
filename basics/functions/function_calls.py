
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

def display_mirrored(word):
  reverse_word = ""
  for letter in reversed(word):
    reverse_word += letter
  
  print("{} | {}".format(word, reverse_word))

def display_repeated(word):
  print("How many times do you want this word repeated?")
  repetitions = int(input())
  repeated = 0

  for repetition in range(repetitions):
    print(word)
    repeated += 1



# Define run function
def run():
  print("Please enter a word:")
  word = input()
  choice = 0

  while (choice != 6):
    print("""Please choose one of the following options for how to proceed:
  [1] Display word in a box
  [2] Display word in lower case
  [3] Display word in upper case
  [4] Display word as mirrored
  [5] Display repeated word
  [6] Quit""")

    choice = int(input())

    if (choice == 1):
      return display_box(word)
    elif (choice == 2):
      return display_lower(word)
    elif (choice == 3):
      return display_upper(word)
    elif (choice == 4):
      return display_mirrored(word)
    elif (choice == 5):
      return display_repeated(word)
    elif (choice == 6):
      break
    else:
      print("{} is not a valid option".format(choice))

# call the run function
#run()
