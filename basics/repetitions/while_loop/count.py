def run():
  # Ask user for how many cables to avoid
  cables_to_avoid = int(input("How many live cables must I avoid?\n"))

  # Declare a control variable
  cables_avoided = 0

  #Avoid cables
  print()

  while (cables_avoided < cables_to_avoid):
    print("Avoiding...", end="")
    cables_avoided += 1
    print("Done!", cables_avoided, "live cables avoided!")

  #Display end message
  print("\nAll live cables have been avoided.")