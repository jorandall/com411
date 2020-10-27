# Define steps function
def steps():
  likelihoods = [
                ("step 1", 50),
                ("step 2", 38),
                ("step 3", 27),
                ("step 4", 99),
                ("step 5", 4)
                ]
  
  return likelihoods

# Define run function
def run():
  likelihoods = steps()

  good_steps = []
  bad_steps = []

  for likelihood in likelihoods:
    if (likelihood[1] >= 50):
      bad_steps.append(likelihood)
    else:
      good_steps.append(likelihood)

  print("Good steps: {}. Bad steps: {}".format(len(good_steps), len(bad_steps)))

#run()

