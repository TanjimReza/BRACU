
def majorityRules(name):
    capitalCount = int(0)
    smallCount = int(0)
    for i in name:
        tempCapitalChar = i.upper()
        #print(tempCapitalChar)
        
        if (i == tempCapitalChar):
            #print("CAPITAL")
            capitalCount += 1 
        else:
            smallCount += 1

    if (capitalCount > smallCount):
        name = name.upper()
        print(name)
    else:
        name = name.lower()
        print(name)
    #No Return

name = input("Enter String: ")
name = name.replace(" ","")
majorityRules(name)