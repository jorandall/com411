# Request ASCII code from user
print("Progam Started!")
print("Please enter an ASCII code:")
code = __abs__(int(input()))

if code in range(32,126):
  print("The character represented by the ASCII code {} is {}".format (code, chr(code)))
else:
  print("Error! Character out of range, cannot convert.")

print("Progam Ended!")