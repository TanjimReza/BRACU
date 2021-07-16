#Hard 02

def palindromic(name):
    nameLength = len(name)
    firstThree = name[nameLength-3] + name[nameLength-2] + name[nameLength-1]
    cutOut = ""
    stopLoop = nameLength - 3
    for i in name[3:stopLoop:1]:
        cutOut = cutOut + i
    if firstThree in cutOut:
        print(firstThree)
    else:
        print("Not Palindrome Substring")
palindromic("fixprefixsuffix")