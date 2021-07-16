num=input("Enter the value of N: ")
aplhaList=input("").split(",")
newList=[]
num = int(num)
for i in range(num):
    newList.append([])
    k=i
    alphaLen = len(aplhaList)
    while k<alphaLen:
        newList[i].append(aplhaList[k])
        k += 3
print(newList)

