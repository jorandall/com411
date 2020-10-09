print("Please enter a marker:")
marker = input()

print("Please enter sequence:")
sequence = input()

# x---x
i_am_counting = False
count = 0

for character in sequence:
  if i_am_counting == True:
    
    if character != marker:
      count += 1
    else:
      print("Found last marker.")
      break
  
  elif character == marker:
    print("Found marker")
    i_am_counting = True

print(count)

    
