#Medium02
n=[]
m=0
highestList=[]
n=int(input("Enter the value of N: "))
count = 0 
while count < n:
    n.append(input("").split())
    count += 1
for i in n:
    sum=0
    for j in i:
        sum=sum+int(j)
    if sum>m:
        m=sum
        temp=i
for i in temp:
    highestList.append(int(i))
print(m)
print(highestList)

