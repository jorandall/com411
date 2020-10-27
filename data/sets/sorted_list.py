# Define function to add observations
def observed():
  observations = []

  for observation in range(5):
    print("Please enter an observation:")
    observed = input()
    observations.append(observed)
  
  return observations

# Define function to remove observations
def remove_observations(observations):
  print("Do you wish to remove an observation (yes/no)?")
  response = input()
  
  #If response is yes, request which observation to remove and action
  if response == "yes":
    print("What observation do you wish to remove?")
    observation_remove = input()
    observations.remove(observation_remove)
    print("Done!")
  # If response is no, continue
  else:
    return

# Define function to run program
def run():
  observations = observed()
  observation_set = set()

  remove_observations()

  for observation in observations:
    observation_set.add(observations)

  print(sorted(observation_set))

run()