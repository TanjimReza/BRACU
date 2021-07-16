
def palindromeCheck(name):
    reversedName = ""
    stringLen = len(name) - 1 
    while(stringLen >= 0):
        reversedName = reversedName + name[stringLen]
        stringLen -=1
    
    return reversedName

name = input("Enter String: ")
name = name.replace(" ","")
result = palindromeCheck(name)

if (name == result):
    print("True")
else:
    print("False")