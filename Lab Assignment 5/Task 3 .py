class Wadiya():
	def __init__(self):
		self.name = 'Aladeen'
		self.designation = 'President Prime Minister Admiral General'
		self.num_of_wife = 100
		self.dictator = True

#Subtask 01

wadiya = Wadiya()

#Subtask 02:

print("Part 1:")
print("Name of President: ", wadiya.name)
print("Designation: " ,wadiya.designation)
print("Number of wife: ", wadiya.num_of_wife)
print("Is he/she a dictator: ", wadiya.dictator)

#Values before changing 
name1 = wadiya.name

#Subtask 03:

print("Part 2:")
wadiya.name = "Donald Trump"
wadiya.designation = "President"
wadiya.num_of_wife = 1 
wadiya.dictator = False

print("Name of President: ", wadiya.name)
print("Designation: " ,wadiya.designation)
print("Number of wife: ", wadiya.num_of_wife)
print("Is he/she a dictator: ", wadiya.dictator)

#Values after changing 

#If one value changes then the rest of them will also get changed

name2 = wadiya.name 

if name1 == name2:
	print("No, changing had no effect on previous value")
else:
	print("Previous information lost")
