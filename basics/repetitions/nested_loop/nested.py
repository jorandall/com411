# Ask the user for how many rows and columns
print("How many rows should I have?")
user_rows = int(input())

print("How many columns should I have?")
user_columns = int(input())

# Display result
print("\nHere I go:\n")

for rows in range(0, user_rows, 1):
  for columns in range(0, user_columns, 1):
    print(":-)", end="")
  print()

print("\nDone!")