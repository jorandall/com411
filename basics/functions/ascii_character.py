# Request ASCII code from user
print("Progam Started!")
print("Please enter an ASCII code between 32 - 126:")
code = abs(int(input()))

if (code >= 32 and code <= 126):
  ascii_letter = chr(code)
  print("The character represented by the ASCII code {} is {}".format (code, ascii_letter))
else:
  print("Error! Character out of range, cannot convert.")

print("Progam Ended!")