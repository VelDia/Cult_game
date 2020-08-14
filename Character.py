# Main Character logic

from random import choice
from character_data import*



class Character:

	def __init__(self, name, age, money, charisma, energy):
		self.name = name
		self.age = age
		self.money = money
		self.charisma = charisma
		self.energy = energy
			
	def greeting(self):
		print(choice(characterGreeting))

	def recruitment(self, bad):
		if bad:
			print(choice(characterRecruitmentBad))
		else:
			print(choice(characterRecruitment))

	def finish_phrase(self):
		print(choice(characterFinishPhrase))




