def run():
  # Ask the user for how many mountains
  print("How many mountains should I display?")
  mountains = int(input())

  # Display mountains
  for mountain in range(mountains):
    print("""
              __
            /  \\_  
          /^    \\
          /  ^    \\_
        _/ ^ ^     ^\\
      /  ^     ^    \\

  """)