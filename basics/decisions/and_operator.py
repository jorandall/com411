def run():
  # Ask user for what they heard and saw
  print("What did I hear?")
  hear = input()
  print("What did I see?")
  see = input()

  # Determine the response
  if (hear == "grrr") and (see == "two red eyes"):
    print("\nThere is a scary creature. I should get out of here!")
  else:
    print("\nI am a little scared but I will continue.")