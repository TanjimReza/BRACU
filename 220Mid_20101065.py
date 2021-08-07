
source = [-10,5,0,0,0,0,-41,14,-4,21]
def result(source, start, size):
    
    firstLargestNegative = 0
    secondLargestNegative = 0
    firstLargestPositive = 0
    secondSmallestPositive = 0 
    sln = 0 
    slp = 0
    #First Traverse
    index = start 
    i = 0 
    while i < size:
        if index == len(source):
            index = 0
            i -= 1 
        else:
            currrentItem = source[index]        
            if currrentItem < firstLargestNegative:
                firstLargestNegative = currrentItem

            if currrentItem > firstLargestPositive:
                firstLargestPositive = currrentItem

            print(source[index])
            index += 1 
        i += 1
    print("===")
    index=start
    i=0
    while(i<size):
        # print(source[index])
        currrentItem = source[index]
        if currrentItem != firstLargestNegative and currrentItem != firstLargestPositive:
            print(source[index], "not")
            
            if currrentItem < sln and currrentItem != 0: 
                sln = currrentItem
                secondLargestNegative = currrentItem
                nextOfSLN = index + 1
            if currrentItem > slp and currrentItem != 0:
                print(currrentItem,"slp")
                slp = currrentItem
                secondSmallestPositive = currrentItem
                prevOfSSP = index - 1

        index=(index+1)%len(source)
        i=i+1
    print("FirstLN:",firstLargestNegative)
    print("FirstLP:",firstLargestPositive)
    print("SecondLN:",secondLargestNegative)
    print("SecondLP:",secondSmallestPositive)


    #Got secondLargestNegative & secondSmallestPositive

    sumOfBoth = secondLargestNegative+secondSmallestPositive
    mulofBoth = secondLargestNegative*secondSmallestPositive
    # print(nextOfSLN)
    # print(prevOfSSP)
    source[nextOfSLN] = sumOfBoth
    source[prevOfSSP] = mulofBoth
       
    index=start
    i=0
    while(i<len(source)):
        # print(source[index])
        index=(index+1)%len(source)
        i=i+1
    
    for i in source: 
        print(i,end=" ")

result(source,start=6,size=6)
