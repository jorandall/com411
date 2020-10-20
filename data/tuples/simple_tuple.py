# Define likelihood function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods))

# Define run function
def run():
  value = likelihood()
  print("Minimum likelihood of falling: {}%".format(value))

run()