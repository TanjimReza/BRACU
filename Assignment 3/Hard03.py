
def usisRocks(password):
    doneCheck = ""
    for char in password:
        ascii_char = ord(char)
        if ascii_char >= 65 and ascii_char <= 90:
            if "CapitalDone" not in doneCheck:
                doneCheck = doneCheck + "CapitalDone"

        if ascii_char >= 97 and ascii_char <= 122:
            if "SmallDone" not in doneCheck:
                doneCheck = doneCheck + "SmallDone"

        if ascii_char >= 48 and ascii_char <= 57:
            if "DigitDone" not in doneCheck:
                doneCheck = doneCheck + "DigitDone"

        if ascii_char == 64 or ascii_char == 36 or ascii_char == 35 or ascii_char == 95:
            if "SpecialCharacterDone" not in doneCheck:
                doneCheck = doneCheck + "SpecialCharacterDone"

    errorCheck(doneCheck)

def errorCheck(errors="doneCheck"):
    errorMessage = ""
    if "DigitDone" in errors:
        if "CapitalDone" in errors:
            if "SmallDone" in errors:
                if "SpecialCharacterDone" in errors:
                    print("OK")
    else:
        if "CapitalDone" not in errors:
            errorMessage = errorMessage + "Uppercase character missing,"
        if "SmallDone" not in errors:
            #print("Lowercase Missing", end=", ")
            errorMessage = errorMessage + "Lowercase Missing,"
        if "DigitDone" not in errors:
            #print("Digit Missing", end=", ")
            errorMessage = errorMessage + "Digit Missing,"
        if "SpecialCharacterDone" not in errors:
            #print("Special Character Missing", end=", ")
            errorMessage = errorMessage + "Special Character Missing,"
    formatErrorMessage(errorMessage)
def formatErrorMessage(errorMessage):
    if errorMessage.endswith(","):
        errorMessageLen = len(errorMessage) - 1
        char = int(0)
        finalErrorMessage = ""
        while char < errorMessageLen:
            finalErrorMessage = finalErrorMessage + errorMessage[char]
            char += 1
    print(finalErrorMessage)

password = input("Enter new password: ")
usisRocks(password)
