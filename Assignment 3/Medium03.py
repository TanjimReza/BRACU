#Medium 03 
def upperCase(name):
  newName = ""
  startN = int(0)
  endN = int(0)
  nameLen = len(name) - 1

  i = int(0)
  while (i < nameLen):
    temUpperCase = name[i].upper()
    if name[i] == temUpperCase:
      if startN == 0:
        startN = i
      else:
        endN = i
    i += 1 

  j = startN + 1

  while(j < endN):
    newName = newName + name[j]
    j += 1
  
  if len(newName) == 0:
    print("BLANK")
  else:
    print(newName)


name = input("Enter String: ")
upperCase(name)