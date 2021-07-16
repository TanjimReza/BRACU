class Joker:
	def __init__(self,name,power,is_he_psycho):
		self.name = name 
		self.power = power
		self.is_he_psycho = is_he_psycho


j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
	print('same')
else:
	print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
	print('same')
else:
	print('different')

#Subtask 2

print("\nQuestion 01: The first if/else block prints the output as ‘different’, but why?\n") 
print("Answer: In the first if/else block the values of j1 & j2 gets checked and as they are not the same, the code under else block gets executed.The reason of them being different is- when we declare j1 and assign values using Joker method it allocates some storage in memory with an address(0x007FE610),then again for j2 it allocates storage in memory with another specified address(0x009CB1D8). These memory addresses are different, they can't be the same. Here Joker is a class, j1 & j2 are objects. They are two different objects containing different data inside them also they are stored in different memory location. Because of all this the first if/else block prints the output as different.\n ")

print("Question 02:The second if/else block prints the output as ‘same’, but why? \n ")
print("Answer: Right before the second if else block at line 22 the value of j2.name is set to 'Heath Ledger' if we look back to line 8 we see the first argument passed is 'Heath Ledger' (j1.name). So in line 23 when j1.name & j2.name gets checked the outcome will be the code under if block as both of them contain the same data. That is why the second if/else block prints the output as same. \n")