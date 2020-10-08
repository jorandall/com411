# Ask user for how many bars
bars_to_charge = int(input("How many bars should be charged?\n"))

# Declare a control variable 
bars_charged = 0

# Display bars

while (bars_charged < bars_to_charge):
  bars_charged += 1
  print("\nCharging:", "█ " * bars_charged)

print("\nThe battery is fully charged.")