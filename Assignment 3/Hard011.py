def hehe(fString,sString):
    finalString = " "
    cChar = int(0)
    print(finalString)
    for i in fString:
        if i in sString:
            print(sString[cChar])
        
        cChar += 1
      
hehe("abc","bcd")