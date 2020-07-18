# Main file

from npc_phrases import*
from character_phrases import*
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

	
	def say_hi(self):	
		print(choice(npc_greeting), self.name)

	def say_answear(self):
		print(choice(npc_answear), self.name)

	def say_bye(self):
		print(choice(npc_final_answear), self.name)


def greeting():
	print(choice(character_greeting))

def recruitment():
	print(choice(character_recruitment))

def finish_phrase():
	print(choice(character_finish_phrase))