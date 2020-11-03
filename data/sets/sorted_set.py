# Define function to add observations
def observed():
  observations = []
  for count in range(5):
    print("Please enter an observation:")
    observations.append( input() )
  return observations

# Define function to remove observations
def remove_observations(observations):
  is_running = True

  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    answer = input()

    if (answer == "yes"):
      print("What observation do you wish to remove?")
      to_remove = input()
      observations.remove(to_remove)
      print("Done!")
    else:
      is_running = False

  return observations


# Define function to run program
def run():
  observations = observed()
  remove_observations(observations)
  observation_set = set()

  for observation in observations:
    occurrences = observations.count(observation)
    observation_set.add( (observation, occurrences) )

  for key, value in sorted(observation_set):
    print(f"{key} observed {value} times.")

# Function call for run
run()