# Define weights function
def sum_weights(beep, bop):
  combined_weight = beep + bop
  print("The combined weight of Beep and Bop is {}.".format(combined_weight))

# Define the calculate average weight function
def calc_avg_weight(beep, bop):
  average_weight = (beep + bop) / 2
  print("The average weight of Beep and Bop is {}.".format(average_weight))

# Define the run function
def run():
  print("What is Beep's weight?")
  beep = int(input())
  print("What is Bop's weight?")
  bop = int(input())

  print("What would you like the calculate (sum or average)?")
  response = input()
  if response == "sum":
    return sum_weights(beep, bop)
  elif response == "average":
    return calc_avg_weight(beep, bop)

# Call the function
run()