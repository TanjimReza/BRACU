#Medium 04
def tooGoodFunction(name):
    if "too good" in name:
    #print("Too Good")
        name = name.replace("too good","excellent")
    print(name)
name = input("Enter string: ")
tooGoodFunction(name)