class Customer:
	def __init__(self,name = None):
		self.name = name
	
	def greet(self,name = None):
		
		if name == None:
			print(f"Hello!")
		else:
			print(f"Hello! {name}")

	def purchase(self,*args):
		count = int(0)
		lst = []
		for item in args:
			count += 1 
			lst.append(item)
		print(f"{self.name}, you purchased {count} item(s):")
		for i in lst:
			print(i)

cusotmer_1 = Customer("Sam")
cusotmer_1.greet()
cusotmer_1.purchase("chips","chocolate","orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")