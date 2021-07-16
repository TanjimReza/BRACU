l = input("Enter first list: ")
l = l.split(" ")
l2 = input("Enter Second list: ")
l2 = l2.split(" ")
f = [] 

for i in l:
    i = int(i)
    for j in l2:
        j = int(j)
        f.append(i*j)

print(f)