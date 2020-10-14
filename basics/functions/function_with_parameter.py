# Define function
def escape_by(plan):
  if plan == "jumping over":
    print("We cannot escape that way! The boulder is too big!")
  elif plan == "running around":
    print("We cannot escape that way! The boulder is moving too fast!")
  elif plan == "going deeper":
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

def run():
  print("What's our plan? (Jumping over, running around, going deeper, or something else?")
  plan = input()
  escape_by(plan)

# Call function
# escape_by("jumping over")
# escape_by("running around")
# escape_by("going deeper")
# escape_by("flying")