n = []
l = True
while l:
    num = input("Enter number: ")
    if num == "stop":
        l = False
    else:
        n.append(int(num))
lis = []
for i in n:
    if i not in lis:
        lis.append(i)
        c = n.count(i)
        print(i,"-",c,"times")
