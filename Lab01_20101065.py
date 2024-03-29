""""
    Name: Tanjim Reza
    Student ID: 20101065
    Section: 08 
    Course: CSE220 
    Faculty Initial: SEJ 
    Assignment No: 01 (LAB)
"""
#------------------------------#
#Task 01: Shift Left k Cells 
#------------------------------#
source=[10,20,30,40,50,60]
def shiftLeft(source, k): 
    for i in range(0,len(source)-k,1): 
        source[i] = source[i+k] 
    for i in range(len(source)-k,len(source),1): 
        source[i] = 0 
    return source
k = 3
shiftLeft(source=source,k=k)
print(source)
#-------------------------------------------------#

#------------------------------#
#Task 02: Rotate Left k Cells
#------------------------------#
source=[10,20,30,40,50,60]
def rotateLeft(source, k): 
    tmp = [0]*k
    for i in range(0,k,1): 
        tmp[i] = source[i]

    for i in range(0,len(source)-k,1): 
        source[i] = source[i+k]

    for i in range(len(source)-k, len(source),1):
        j = len(source) - k
        source[i] = tmp[i-j]
k = 3
rotateLeft(source=source, k=k)
print(source)
#-------------------------------------------------#

#------------------------------#
#Task 03: Remove an element from array
#------------------------------#
source=[10,20,30,40,50,0,0]
def remove(source,size,idx): 
    for i in range(idx,len(source)-1,1): 
        source[i] = source[i+1]     
    return source
size = 5
idx = 2
remove(source=source,size=size,idx=idx)
print(source)
#-------------------------------------------------#

#------------------------------#
#Task 04: Remove all occurences of a particular element  array
#------------------------------#
source=[10,2,30,2,50,2,2,60,0,0]
def removeAll(source,size,element):
    while element in source:
        for i in range(0,len(source)-1,1): 
            if source[i] == element:
                j = i 
                for k in range(j,len(source)-1,1): 
                    source[k] = source[k+1]          
    return source
size = 8 
element = 2
removeAll(source=source,size=size,element=element)
print(source)
#-------------------------------------------------#

#------------------------------#
#Task 05: Splitting an Array 
#------------------------------#

source =  [1, 1, 1, 2, 1]
def SplitArray(source): 
    total = 0
    count = 0 
    for i in range(len(source)): 
        total += source[i]
    for i in range(0,len(source),1):
        leftSum = 0 
        rightSum = 0 
        for j in range(0,i+1,1): 
            leftSum += source[j]
        rightSum = total-leftSum        
        if leftSum == rightSum: 
            return print("true")
        count += 1
    if count == len(source): 
        return print("false")            
SplitArray(source)

#-------------------------------------------------#

#------------------------------#
#Task 06: Array Series
#------------------------------#
def arraySeries(n):
    mylist = [0]*n*n
    numberedlist = list(range(1,n+1))
    x = 0

    for i in range(n):
        for j in range(n):   
            if i+j>=n-1:
                mylist[x] = numberedlist[n-j-1]           
            x = x+1
    return mylist
n = 4
result = arraySeries(n)
print(result)

#------------------------------#
#Task 07: Max Bunch Count
#------------------------------#
source = [1, 2, 2, 3, 4, 4, 4]
def maxBunchCount(source): 
    max = 1
    count = 1
    for i in range(0,len(source)-1,1):
        if source[i] == source[i+1]: 
            count += 1
        else: 
            count = 1
        if count > max: 
            max = count
    return max
result = maxBunchCount(source=source)
print(result)
#-------------------------------------------------#

#------------------------------#
#Task 08: Repetition
#------------------------------#
"""In this problem, I am considering 0 as valid numbers and I did not know that we could
use append function until after I have solved this problem 
"""


# source = [4,5,6,4,6,4,3,6,6,4]
source = [3,4,6,3,4,7,4,6,8,6,6]
def repetitionCheck(source): 
    status = False
    tmp = [""]*len(source)
    checkedItem = [0]*len(source)
    for item in range(0,len(source),1):
        currentItem = source[item]
        c = 0
        if currentItem not in checkedItem:
            checkedItem[item] = currentItem
            for j in range(0,len(source)): 
                if source[j] == currentItem:
                    c += 1 
            if c > 1: 
                tmp[item] = c
    for j in range(len(tmp)):
        check = tmp[j]
        if check != "": 
            c = 0
            for k in range(len(tmp)): 
                check2 = tmp[k]
                if check2 != "": 
                    if check == check2: 
                        c += 1
            if c > 1: 
                status = True
    return status
repetitionCheckResult = repetitionCheck(source=source)
print(repetitionCheckResult)

#------------------------------#
#Task 01 Circular Array: Palindrome
#------------------------------#
source =  [20,10,0,0,0,10,20,30] 
def palindrome(source,start,size):
    index = start
    i = 0
    newArray = []
    newArray2 = []
    while i<size:
        if index == len(source):
            index = 0
            i -= 1
        else:
            newArray.append(source[index])
            index += 1
        i += 1
    for i in range(len(newArray)-1,-1,-1):
        newArray2.append(newArray[i])
    if newArray==newArray2: 
        return True
    else: 
        return False
start = 5
size =5
result = palindrome(source=source,start=start, size=size)
print(result)
#----------------------------------------------------------#



#------------------------------#
#Task 02 Circular Array: Intersection
#------------------------------#
"""
    I am not sure I am allowed to solve this problem like I did. But in the last time this is what I could do. 
    I apologize if I am doing anything that I should not do

"""
source =  [40,50,0,0,0,10,20,30]
source2 = [10,20,5,0,0,0,0,0,5,40,15,25]
def intersection(source,source2,start_1,start_2,size_1,size_2):
    start_2 = "I am not using this"
    size_2 = "Not using this too"
    index = start_1
    i = 0
    newArray = []
    while i<size_1:
        if index == len(source):
            index = 0
            i -= 1
        else:
            if source[index] in source2: 
                if source[index] not in newArray:
                    newArray.append(source[index])
            index += 1
        i += 1
    return newArray
start_1 = 5
size_1 =5
start_2 =8
size_2 =7
result = intersection(source=source,source2=source2,start_1=start_1, size_1=size_1,start_2=start_2,size_2=size_2)
print(result)

#------------------------------#
#Task 03 Circular Array: 
#------------------------------#
"""
    I think I need to study more to be able to solve this one. I am trying. 

"""

""" Final Output serially 

[40, 50, 60, 0, 0, 0]
[40, 50, 60, 10, 20, 30]
[10, 20, 40, 50, 0, 0, 0]
[10, 30, 50, 60, 0, 0, 0, 0, 0, 0]
true
[0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
3
False
True
[10, 20, 40]

"""
