def run():
  # Greet user and request a letter
  print("Progam Started!")
  print("Please enter a letter:")
  letter = input()

  # Convert the letter to Ascii code and print result:

  if len(letter) == 1:
    print ("The ASCII code for {} is: {}".format(letter, ord(letter)))
  else:
    print("Error. Single letter not entered, cannot convert.")

  # End program
  print("Program Ended!")

