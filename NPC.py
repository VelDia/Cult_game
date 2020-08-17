# NPC logic

from npc_data import*
from random import choice

class Person:

	believers = 0

	def __init__(self, name, age, gender, charisma, motivation, element):
		self.name = name
		self.age = age
		self.gender = gender
		self.charisma = charisma
		self.motivation = motivation
		self.element = element
		Person.believers += 1
		
		"""
		
		[name] - NPC name
		[age] - NPC age (from 18 to 90)
		[money] - amount of money that NPC have (smart random)
		[charisma] - level of charisma of character (smart random)
		[energy] - level of energy of character (smart random)
		[element] - element of character (0, 1, 2) == (rock, paper, scissors)
		
		"""


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
