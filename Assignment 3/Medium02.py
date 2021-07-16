#Mediium02

def kindChecker(userInput):
    integerCount = int(0)
    userInputLength = len(userInput) 
    digits = {'1','2','3','4','5','6','7','8','9','0'}
    for i in userInput:
        if i in str(digits):
            integerCount += 1 #If integerCount > 0 then can't be a number
    if(integerCount == userInputLength): #If every single one is a digit then it's a number
        print("NUMBER")
    elif(integerCount == 0): ##If integerCount 0 then no digits in input, it must be a string
        print("WORD")
    else: #If not above two, then must be this one 
        print("MIXED")
userInput = input("Enter: ")
kindChecker(userInput)