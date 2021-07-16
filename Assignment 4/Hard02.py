name=input("")
niceOrder = ""
for i in range(97,123): #SMALL
    for j in name:
        if chr(i)==j: 
            niceOrder=niceOrder+j
for i in range(65,91): #CAPITAL
    for j in name:
        if chr(i)==j:
            niceOrder=niceOrder+j
for i in range(1,10,2): #ODD
    for j in name:
        if str(i)==j or j=='0':
            niceOrder=niceOrder+j
for i in range(2,10,2): #EVEN
    for j in name:
        if str(i)==j:
            niceOrder=niceOrder+j
for i in ('@','#','$','&','_'): #SPECIAL
    for j in name:
        if i==j:
            niceOrder=niceOrder+j
 
print(niceOrder)