# Ask user which way Beep is painting with an if...elif...else statement
print("Towards which direction should I paint? (up, down, left or right?)")
direction = input()

if (direction == "top"):
  print("I am painting in an upward direction!")
elif (direction == "down"):
  print("I am painting in a downward direction!")
else:
  print("I am painting in a sideways direction!")