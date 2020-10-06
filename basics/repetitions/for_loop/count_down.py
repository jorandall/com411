# Ask user how far away we are
print("How far are we from the cave?")
distance = int(input())

# Display the result
print()

for steps in range(distance, 0, -1):
  print(steps, "steps remaining")

print("\nWe've reached the cave!")