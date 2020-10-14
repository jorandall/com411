# Define weights function
def sum_weights(beep, bop):
  combined_weight = beep + bop
  return combined_weight

# Define the calculate average weight function
def calc_avg_weight(beep, bop):
  average_weight = (beep + bop) / 2
  return average_weight

# Define the run function
def run():
  print("What is Beep's weight?")
  beep = int(input())
  print("What is Bop's weight?")
  bop = int(input())

  print("What would you like the calculate (sum or average)?")
  response = input()

  if (response) == "sum":
    sum_answer = sum_weights(beep, bop)
    print("The total weight of Beep and Bop is {:.2f}.".format(sum_answer))
  elif response == "average":
    average_answer = calc_avg_weight(beep, bop)
    print("The average weight of Beep and Bop is {:.2f}.".format(average_answer))
  else:
    print("Action not recognised.")

# Call the function
#run()