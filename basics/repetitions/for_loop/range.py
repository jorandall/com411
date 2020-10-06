# Ask user for level of brightness
print("What level of brightness is required?")
brightness_desired = int(input())

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 2):
  print("Beep's brightness level:", "*" * brightness)
  print("Bop's brightness level:", "*" * brightness)
  print()

print("\nAdjustments complete")