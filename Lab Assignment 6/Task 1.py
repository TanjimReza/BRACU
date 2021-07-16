class Calculator(object):
	def __init__(self):
		print("Let's Calculate!")
	def add(self,a,b):
		return a+b
	def subtract(self,a,b):
		return a-b
	def multiply(self,a,b):
		return a*b
	def divide(self,a,b):
		return a/b

a = Calculator()
fVal = int(input())
sVal = input()
tVal = int(input())
nl = "\n" #as i cant use quotation marks inside advanced print function, I'm using this variable to do the intended job
if sVal == "+":
	result = a.add(fVal,tVal)
	print(f"Value 1: {fVal}{nl}Operator: {sVal}{nl}Value 2: {tVal}{nl}Result: {result}")
elif sVal == "-":
	result = a.subtract(fVal,tVal)
	print(f"Value 1: {fVal}{nl}Operator: {sVal}{nl}Value 2: {tVal}{nl}Result: {result}")
elif sVal == "*":
	result = a.multiply(fVal,tVal)
	print(f"Value 1: {fVal}{nl}Operator: {sVal}{nl}Value 2: {tVal}{nl}Result: {result}")
else:
	result = a.divide(fVal,tVal)
	print(f"Value 1: {fVal}{nl}Operator: {sVal}{nl} Value 2: {tVal}{nl}Result: {result}")
