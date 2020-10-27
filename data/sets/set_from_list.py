# Define function to see what has been observed
def observed():
  observations = []

# Ask the user for input 7 times and add to the list
  for count in range(7):
    print("Please enter an observation:")
    observed = input()
    observations.append(observed)

# Return the compiled list
  return observations


# Define run function
def run():
  print("Counting observations...")
  observations = observed()
  observation_set = set()

  for observation in observations:
    occurrences = observations.count(observation)
    observation_set.add( (observation, occurrences) )
    
  for key, value in observation_set:
    print(f"{key} observed {value} times.")

# Function call for run
run()