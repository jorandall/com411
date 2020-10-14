def run():
  # Ask user for a number
  print("Please enter a number:")
  number = int(input())

  # Declare control variables
  count = 0
  total = 1

  # Calculate factorial
  while (count < number):
    count = count + 1
    total = total * count

  # Display result
  print("The factorial is", total)
