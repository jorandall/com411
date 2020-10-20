# Define likelihood function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)

  return min(likelihoods), max(likelihoods)

# Define run function
def run():
  values = likelihood()

  # Index to the nested list (min and max)
  print("Minimum likelihood of falling: {}%".format(values[0])) 
  print("Maximum likelihood of falling: {}%".format(values[1]))