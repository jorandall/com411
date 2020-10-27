# Define function to see what has been observed
def observed():
  observations = []

# Ask the user for input x7
  for count in range(7):
    print("Please enter an observation:")
    observed = input()
    observations.append(observed)

  return observations


# Define run function
def run():
  print("Counting observations...")
  observations = observed()
  observation_set = set()

  for observation in observations:
    observation_set.add((observation, observations.count(observation)))
    
  print(observation_set)

# Function call for run
run()