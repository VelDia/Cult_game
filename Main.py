# Main file

from Phrases import*
from random import choice


class Person:

	believers = 0	# our believers

	def __init__(self, name, age, gender, charisma, motivation): # with initializing person passing its parameters
		self.name = name
		self.age = age
		self.gender = gender
		self.charisma = charisma
		self.motivation = motivation
		Person.believers += 1
		
	def __del__(self):	# delete object and decrese amount of believers
		Person.believers -= 1

	def say_Hi(self):	# type of greeting for NPC
		print(choice(greeting), self.name)

	def say_Answear(self):
		print(choice(answear), self.name)

	def say_Bye(self):
		print(choice(answear), self.name)

	