# Define function for short patterns
def short_pattern():
  pattern = {
    "sequence":"101", 
    "occurrences": 5
    }
  return pattern

# Define function for medium patterns
def medium_pattern():
  pattern = {
    "sequence":"111000",
    "occurrences": 25
    }
  return pattern

# Define function for long patterns
def long_pattern():
  pattern = {
    "sequence": "1100110011001100",
    "occurrences": 50
    }
  return pattern

# Define function to run the program
def run():
  print("Analysing patterns...")
  patterns = {
    "short sequence": short_pattern(),
    "medium sequence": medium_pattern(),
    "long sequence": long_pattern()
    }
  
  print(patterns)

run()