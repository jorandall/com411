def run():
  # Ask the user to define which markings they've seen
  print("What strange markings do you see?")
  markings = input()

  # Displaying the characters
  print("\nIdentifying...\n")

  for count in range(0, len(markings), 1):
    print("Index", count, ":", markings[count])

  print("\nDone!")
