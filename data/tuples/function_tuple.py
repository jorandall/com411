# Define likelihood function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)

  return min(likelihoods), max(likelihoods)

def run():
  values = likelihood()
  print("Minimum likelihood of falling: {}%".format(values[0]))
  print("Maximum likelihood of falling: {}%".format(values[1]))