# Ask user to input sequence
print("Please enter a sequence of characters consisting of dashes and two markers:")
sequence = input()

print("Please enter the character you've used for the marker:")
marker = input()

# Find markers

marker1 = -1
marker2 = -1

for position in range (0, len(sequence), 1):
  letter = sequence[position]
  
  if (letter == marker):
    if (marker1 == -1):
      marker1 = position
    else:
      marker2 = position

# Display result
print("The distance between the markers is", marker2 - marker1 - 1)



