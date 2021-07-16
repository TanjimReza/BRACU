class Student:
	def __new__(cls, *args, **kwargs):
		print("Object Created")
		return object.__new__(Student)
	def __init__(self,name,i,cg,credit):
		self.name = name
		self.id = i
		self.cg = cg
		self.credit = credit
x = input().split(" ")
s1 = Student(x[0], int(x[1]), float(x[2]),float(x[3]))
print(s1.name, s1.id, s1.cg, s1.credit)