def run():
  # Ask user for type of adventure
  print("What type of adventure should I have?")
  adventure = input()

  # Determine the message to display
  if ((adventure == "scary") or (adventure == "short")):
    print("Entering the dark forest!")
  elif ((adventure == "safe")or (adventure == "long")):
    print("Taking the safe route!")
  else:
    print("Not sure which route to take.")