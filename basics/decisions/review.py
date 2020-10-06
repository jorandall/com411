# Introduction to Beep and ask user to continue
print("Hello! My name is Beep. Shall we take an adventure together?")
adventure = input()

# Going on the adventure

if (adventure == "yes"):
  print("Let's go! \nShall we go to the forest or the beach?")
  lets_go = input()
  if (lets_go == "forest"):
    print("It's dark here, I want to go home!")
  else:
    print("It's lovely here, let's have a picnic!")
else:
  print("Okay, how about we play a game?")
  game = input()

  # Play a game

if (game == "yes"):
  print("Shall we play hind and seek?")
  play = input()
  if (play == "yes"):
    print("OK, you hide first!")
  else:
    print("Well, I don't want to play anything else!")
else:
  print("You're no fun.")

# Ask user what they want to do

print("OK, so what do you want to do?")
response = input()

# Determine response

if (response == "nothing") or (response == "leave me alone"):
  print("I am sad you don't want to be friends.")
elif (response == "play a game") or (response == "go on an adventure"):
  print("Too late now, you had your chance.")
else:
  print("Beep is sad and lonely.")