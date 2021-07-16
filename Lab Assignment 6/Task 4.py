class Cat:
	def __init__(self,color = "White",work = "sitting"):
		self.color = color
		self.work = work 

	def printCat(self):
		n = self.color
		stat = self.work
		print(f"{n} cat is {stat}")
	def changeColor(self,newColor):
		self.color = newColor

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()