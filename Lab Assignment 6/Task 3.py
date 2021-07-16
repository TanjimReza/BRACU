class Panda:
	def __init__(self,name,gender,age):
		self.name = name 
		self.gender = gender
		self.age = age

	def sleep(self,hours = None):
		food = ""
		if hours != None:
			if hours <= 5 and hours >= 3:
				food = self.name + " sleeps " + str(hours) + " daily and should have "+ "Mixed Veggies"
			elif hours <= 8 and hours >= 6:
				food = self.name + " sleeps " + str(hours) + " daily and should have "+ "Eggplant & Tofu"
			elif hours <= 11 and hours >= 9:
				food = self.name + " sleeps " + str(hours) + " daily and should have " + "Broccoli Chicken"
		else:
			food = self.name + "'s duration is unknown thus should have only " + "bamboo leaves"

		return food 

panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))

print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())