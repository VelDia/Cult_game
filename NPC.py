# NPC logic

from npc_data import*
from random import choice

class Person:

	believers = 0

	def __init__(self, name, age, gender, charisma, motivation):
		self.name = name
		self.age = age
		self.gender = gender
		self.charisma = charisma
		self.motivation = motivation
		Person.believers += 1
		
	def __del__(self):
		Person.believers -= 1
	
	def sayHi(self):	
		print(choice(npcGreeting) + ' I\'m ' + self.name)

	def answer(self, correct):
		if correct:
			print(choice(npcPositiveAnswear))
		else:
			print(choice(npcNegativeAnswear))

	def sayBye(self, positive):
		if positive:
			print(choice(npcFarewellPositive))
		else:
			print(choice(npcFarewellNegative))
