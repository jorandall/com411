def run():
  # Calculate the sum
  print("Calculating the sun of the first 100 numbers...")

  # Declare the control variable
  number = 1

  # Calculate sum of first 100 numbers
  total = 0

  while (number <= 100):
    total = total + number
    number = number + 1

  # Display the result
  print("...Done! The answer is", total)