# Main file

from Greeting.py import greeting
from random import choice

class Person:
	def sayHi(self):

		print(choice(greeting))