firstList = input("Enter first list: ")
firstList = firstList.split(",")
del firstList[-1]
secondList = input("Enter Second list: ")
secondList = secondList.split(",")

finalList = firstList + secondList
print(finalList)
