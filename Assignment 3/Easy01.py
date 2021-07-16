
def excellentFunction(name):
    updatedName = ""
    vowels = {'a','e','e','o','u'}
    vowelCount = 0
    tmp = int(0)
    for i in name:
        if i in str(vowels):
            #print(i + " is a vowel.")
            vowelCount += 1
            #rint("Current Vowel: ", end = " ")
            #print(name[tmp])
        else:
            #print("Updated name current " + updatedName)
            #print("Consonant: ", end = " ")
            #print(name[tmp])
            updatedName = updatedName + name[tmp]
            #print("Updated name changed:  " + updatedName)
        tmp += 1
        #print(updatedName + str(vowelCount))
    finalOutput = updatedName + str(vowelCount)
    return finalOutput
name = input("Enter String: ")
name = name.casefold()
name = name.replace(" ","")
result = excellentFunction(name)
#print("Out of function: " + str(result))
print(result)