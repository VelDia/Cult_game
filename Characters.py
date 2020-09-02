# Main Character logic
# And NPC logic

from random import choice, randint
from character_data import*

from npc_data import*

#================================================
#			  Main Character logic
#================================================

class Character:

	def __init__(self, name, age, gender, money, charisma, energy, element):
		self.name = name
		self.age = age
		self.gender = gender
		self.money = money
		self.charisma = charisma
		self.energy = energy
		self.element = element

		"""
		
		[name] - name of character (Player choose at the beginning)
		[age] - age of character (at the beginning equals to 21)
		[gender] - gender of a character (0 - female or 1 - male)
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

	def finish_phrase(self, bad):
		if bad:
			print(choice(characterFinishPhraseBad))
		else:
			print(choice(characterFinishPhrase))


#================================================
#			Creating Main Character
#================================================

def GetName():
	characterName = input("Enter your name: ")
	return characterName

def GetGender():
	CharacterGender = input("Entere your gender: ")
	if CharacterGender == '1':
		CharacterGender = 1
	else:
		CharacterGender = 0
	
	return CharacterGender


MainCharacter = Character(GetName(), 21, GetGender(), 0, 0, 100, 0)

def SkipTutorial():
	# actions with MainCharacter characteristics
	# Add soon
	pass

#================================================
#================================================



#================================================
#					NPC logic
#================================================

class NPC:

	believers = 0

	def __init__(self, name, age, gender, charisma, motivation, element):
		self.name = name
		self.age = age
		self.gender = gender
		self.charisma = charisma
		self.motivation = motivation
		self.element = element
		#NPC.believers += 1
		
		"""
		
		[name] - NPC name
		[age] - NPC age (from 18 to 80)
		[gender] - gender of NPC (smart random) (0 - female, 1 - male)
		[charisma] - level of charisma of character (smart random)
		[motivation] - motivation to listen to Main Character (smart random)
		[element] - element of character (0, 1, 2) == (rock, paper, scissors)
		
		"""

	def __del__(self):
		NPC.believers -= 1
	
	def greeting(self):	
		print(choice(npcGreeting) + ' I\'m ' + self.name)

	def phrase(self, bad):
		if bad:
			print(choice(npcAnswearBad))
			self.motivation -= randint(1, 5) # Need to add smart random  parameters
		else:
			print(choice(npcAnswear))
			self.motivation += randint(1, 5) # Here too

	def farewell(self, bad):
		if bad:
			print(choice(npcFarewellBad))
			self.motivation -= randint(1, 5) # Here too
		else:
			print(choice(npcFarewell))
			self.motivation += randint(1, 5) # Here too
	
	def add_believer(self):
		NPC.believers +=1

# Need to dislocate it
def SmartRandom(level):	# For creating appropriate NPC
	"""
	SmartRandom

	Args:
		level (int): takes level from 0 to 4 (easy, medium, hard, extreme, ureal)

	Returns:
		tuple: ready for creating new class 'NPC' member data  
	"""	

	if level == 0:	# Easy
		MIN_charisma = 0
		MAX_charisma = MainCharacter.charisma + 2

		MIN_motivation = 50
		MAX_motivation = 70
	elif level == 1:	# Medium
		MIN_charisma = MainCharacter.charisma 
		MAX_charisma = MainCharacter.charisma + 5

		MIN_motivation = 50
		MAX_motivation = 60
	elif level == 2:	# Hard
		MIN_charisma = MainCharacter.charisma + 5
		MAX_charisma = MainCharacter.charisma + 15

		MIN_motivation = 30
		MAX_motivation = 50
	elif level == 3:	# Extreme
		MIN_charisma = MainCharacter.charisma + 15
		MAX_charisma = MainCharacter.charisma + 35

		MIN_motivation = 20
		MAX_motivation = 40
	elif level == 4:	# Unreal
		MIN_charisma = MainCharacter.charisma + 35
		MAX_charisma = MainCharacter.charisma + 65

		MIN_motivation = 0
		MAX_motivation = 30
	
	age = randint(18, 80)
	gender = randint(0, 1)
	charisma = randint(MIN_charisma, MAX_charisma)
	motivation = randint(MIN_motivation, MAX_motivation)
	element = randint(0, 2)	

	if gender == 0:
		name = choice(npcFemaleNames)
	else:
		name = choice(npcMaleNames)

	return name, age, gender, charisma, motivation, element


# Test comment
