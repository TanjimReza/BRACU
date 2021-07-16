#Hard01
niceList=[]
counter = True
while counter:
    num=input()
    if num=="STOP":
        break
    niceList.append(num.split())
for i in niceList:
    defaultTesult="UB Jumper"
    num=[]
    for j in range(len(i)-1):
        n=int(i[j])-int(i[j+1])
        if n<0:
            n=n*-1
        num.append(n)
    for k in range(1,len(i)):
        if k not in num:
            defaultTesult="Not UB Jumper" #Need to change in this case 
    print(defaultTesult)

