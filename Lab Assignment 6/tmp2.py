class Vehicle:
	def __init__(self,x=int(0),y=int(0),cList = [0,0]):
		self.x = x 
		self.y = y
		self.cList = cList
		self.cTuple = tuple(cList)
		print(self.cTuple)
	def moveUp(self):
		self.cList[1] = self.cList[1] + 1
		self.cTuple = tuple(self.cList)

	def print_position(self):
		print(self.cTuple)

car = Vehicle()
car.print_position() #initial
print("first")
car.moveUp()
car.print_position()
print("second")
car.moveUp()
car.print_position()
car.moveUp()
car.print_position()