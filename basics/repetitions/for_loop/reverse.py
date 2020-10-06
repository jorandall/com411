# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Reversing
print("\nReversing...\nThe phrase is:", end=" ")

# Display result
for position in range(len(phrase) -1, -1, -1):
  print(phrase[position], end="")