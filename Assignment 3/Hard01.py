# Hard - 01
def giveMeCommon(name):

    niceList = name.split(",")
    firstString = niceList[0] #first part in one and the second part is on another one
    secondString = niceList[1]
 
    finalString = ""
 
    for i in firstString: 
        if i in secondString: 
            finalString = finalString + i
 
    for i in secondString: 
        if i in firstString: 
            finalString = finalString + i
 
    if finalString == "":        
        print("Nothing in common.")
 
    else: 
        print(finalString)

name = input("Enter Strings: ")
giveMeCommon(name)