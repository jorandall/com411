# Ask user for how many bars
print("How many bars should be charged?")
bars_to_charge = int(input())

# Declare a control variable 
bars_charged = 0

# Display bars
print()

while (bars_charged < bars_to_charge):
  bars_charged = bars_charged + 1
  print("Charging:", "█ " * bars_charged)

print("\nThe battery is fully charged.")