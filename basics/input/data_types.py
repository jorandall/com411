 
def run():
  
  # Ask for user's details to work out their BMI
  print("What is your name human?")
  name = input()

  print("How old are you (in years?)")
  age = int(input())

  print("How tall are you (in metres?)")
  height = float(input())

  print("How much do you weight (in kilograms?)")
  weight = float(input())

  # bmi= weight / (height*height)     #Calculation for working out BMI, transferrable in other languages
  bmi = weight / (height ** 2)        # Calculation for working out BMI, Python only

  print("{} you are {} years old and your bmi is {:.2f}.".format(name, age, bmi))  # Formatted to .2 decimal places