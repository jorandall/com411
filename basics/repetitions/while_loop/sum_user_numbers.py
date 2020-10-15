def run():
  # Ask user for numbers
  print("How many numbers should I sum up?")
  number_to_sum = int(input())

  # Delcare the control variable
  summed = 0

  # Display blank line
  print()

  # Sum numbers
  total = 0

  while (summed < number_to_sum):
    print("Please enter number", summed, "of", number_to_sum, ":")
    number = int(input())
    total = total + number
    summed = summed + 1

  # Display result
  print("The answer is", total)