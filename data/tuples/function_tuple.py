# Define likelihood function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)

  return("Minimum likelihood of falling: {}%.".format(min(likelihoods)))
  return("Maximum likelihood of falling: {}%.".format(max(likelihoods)))

# Likelihood function call
print(likelihood())
print(likelihood())
