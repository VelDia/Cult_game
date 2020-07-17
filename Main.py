# Main file

from Greeting import greeting
from random import choice

class Person:
	def __init__(self, name):
		self.name = name

	def sayHi(self):
		print(choice(greeting), self.name)

