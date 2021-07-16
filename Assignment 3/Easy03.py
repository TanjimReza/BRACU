
def beautifyString(name):
    lastThreeChar = ""
    nameLength = len(name)
    if (nameLength >= 4):
        lastThreeChar = name[nameLength-3] + name[nameLength-2] + name[nameLength-1]
        if (lastThreeChar == "ful"):
            name = name + "ly"
        else:
            name = name + "ful"
        print(lastThreeChar)
        print(name)
    else:
        print(name)

    #No Return 

name = input("Enter String: ")
name = name.casefold()
beautifyString(name)
