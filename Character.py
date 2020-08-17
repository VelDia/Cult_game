# Main Character logic

from random import choice
from character_data import*



class Character:

	def __init__(self, name, age, money, charisma, energy, element):
		self.name = name
		self.age = age
		self.money = money
		self.charisma = charisma
		self.energy = energy
		self.element = element

		"""
		
		[name] - name of character (Player choose at the beginning)
		[age] - age of character (at the beginning equals to 21)
		[money] - amount of money that character have (at the beginning equals to 0)
		[charisma] - level of charisma of character (at the beginning equals to 0)
		[energy] - level of energy of character (at the beginning equals to 100)
		[element] - element of character (0, 1, 2) == (rock, paper, scissors)
		
		"""
			
	def greeting(self):
		print(choice(characterGreeting))

	def recruitment(self, bad):
		if bad:
			print(choice(characterRecruitmentBad))
		else:
			print(choice(characterRecruitment))

	def finish_phrase(self):
		print(choice(characterFinishPhrase))




