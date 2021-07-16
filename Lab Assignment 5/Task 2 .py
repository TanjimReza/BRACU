class Flower:
	def __init__(self):
		self.name = ""
		self.color = ""
		self.num_of_petal = ""

flower1 = Flower();
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2.num_of_petal)

#Subtask 01:
#Address of flower1 
print(flower1)
#Address of flower2
print(flower2)

#Subtask 02:

addressOfFlower1 = flower1
addressOfFlower2 = flower2
if addressOfFlower1 == addressOfFlower2:
	print("They are same")
else:
	print("They are differentb")

