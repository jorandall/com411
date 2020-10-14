def run():
  # Import module
  import random as rnd

  # Ask user for number range
  print("Please enter the minimum value:")
  min = int(input())
  print("Please enter the maximum value:")
  max = int(input())

  # Control variable
  number  = rnd.randrange(min, max)

  # Ask user to guess the number
  print("I am thinking of a number between {} and {}. Can you guess what it is?".format(min, max))

  # Loops for guesses

  guess = 0

  while guess != number:
    guess = int(input())

    if (guess == number):
      print("Congratulations! You guessed my number!")
      break
    elif (guess < number):
      print("Your guess is too low.\nTry again:")
    else:
      print("Your guess is too high.\nTry again:")