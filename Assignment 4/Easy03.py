#Easy03
numberList = []
i = int(0)
while(i < 10):
    num = int(input("Enter a number: "))
    if num not in numberList:
        numberList.append(int(num))
    else:
        print("Number exists!")
        i -= 1
    i += 1
print(numberList)