# Main Character logic
# And NPC logic

from random import choice, randint
#from Tutorial import Visit
from character_data import characterGreeting
from npc_data import*
import time, threading
#================================================
#			  Main Character logic
#================================================
class People:
	def __init__(self, name, gender, age, picture):
		self.name = name
		self.gender = gender
		self.age = age
		self.picture = picture

	def GetName(self):
		Name = input("Enter character name: ")
		return Name
	
	def GetGender(self):
		Gender = int(input("Enter your gender: (\"0\" for female, \"1\" for male, \"9\" for a random gender)  "))
		if Gender == 9:
			Gender = randint(0,1)
		if Gender == 0:
			strGender = 'female'
		elif Gender == 1:
			strGender = 'male'	
		else:
			print('Error: wrong gender initialization...')
		return strGender

	def get_picture(self, age, gender):
		if gender == 0:
			print("female") #enter/search the folder with girl`s pictures
		elif gender == 1:
			print("male") #enter/search the folder with boy`s pictures
		if age < 30:
			print("young person")
			#find and attach the picture of the young person
		elif age >= 30 and age <=50:
			print("middle-aged person")
			#find and attach the picture of the middle-aged person
		else: 
			#or elif age >= 50:... and then else: print("Unable to attach the picture")
			print("old person")
			#find and attach the picture of the old person

class Character(People):

	believers = 0
	level = 0
	money = 0

	def __init__(self, name, age, gender, money, charisma, energy, level, believers, picture):
		People.__init__(self, name, gender, age, picture)
		self.money = money
		self.charisma = charisma
		self.energy = energy
		self.level = level
		self.believers = believers
		self.picture = picture

		"""
		
		[name] - name of character (Player choose at the beginning)
		[age] - age of character (at the beginning equals to 21)
		[gender] - gender of a character (0 - female or 1 - male)
		[money] - amount of money that character have (at the beginning equals to 0)
		[charisma] - level of charisma of character (at the beginning equals to 0)
		[energy] - level of energy of character (at the beginning equals to 100)
		#[element] - element of character (0, 1, 2) == (rock, paper, scissors)
		[level] - literally, the level of the character, which indicates how much stages the main character has gone through...
		[believers] - the amount of people, who believe in religion of the character
		
		"""
	
			
	def greeting(self):
		print(choice(characterGreeting))

	def recruitment(self, ListOfPhrases, ListOfPhrasesBad):
		print('1.',choice(ListOfPhrases))
		print('2.',choice(ListOfPhrasesBad))
		answ = int(input('Choose the answer: '))
		if answ == 1:
			bad = False
		elif answ == 2:
			bad = True
		else:
			print('Something went wrong try again')
		return bad
	'''
	def recruitment(self, bad):
		if bad == True:
			print(choice(characterRecruitmentSoftBad))
		else:
			print(choice(characterRecruitmentSoft))


	def finish_phrase(self, bad):
		if bad == True:
			print(choice(characterFinishPhraseBad))
		else:
			print(choice(characterFinishPhrase))
	'''	
	def add_believer(self):
		self.believers += 1

	def level_up(self):
		self.level += 1

#================================================
#			Creating Main Character
#================================================
'''
def aTutorial():
	global MainCharacter
	MainCharacter = Character(Character.GetName(Character), 21, Character.GetGender(Character), 0, 100, 0, 0, 0, Character.get_picture(Character, 21, Character.GetGender(Character)))
	Visit()
'''

def SkipTutorial():
	# actions with MainCharacter characteristics
	# Add soon
	pass

#================================================
#================================================

MainCharacter = Character('Default name', 21, 0, 0, 50, 100, 1, 0, 0)

#================================================
#					NPC logic
#================================================

class NPC(People):

	def __init__(self, name, age, gender, motivation, picture):
		People.__init__(self, name, gender, age, picture)
		self.motivation = motivation

		"""
		[name] - NPC name
		[age] - NPC age (from 18 to 80)
		[gender] - gender of NPC (smart random) (0 - female, 1 - male)
		[charisma] - level of charisma of character (smart random)
		[motivation] - motivation to listen to Main Character (smart random)
		#[element] - element of character (0, 1, 2) == (rock, paper, scissors)
		[picture] - the number of the picture which will be shown on the screen when the NPC is shown

		"""
	
	def greeting(self):	
		print(choice(npcGreeting) + ' I\'m ' + self.name)

	def phrase(self, bad):
		if bad == True:
			print(choice(npcAnswearBad))
			self.motivation -= randint(5, 10) # Need to add smart random  parameters
		else:
			print(choice(npcAnswear))
			self.motivation += randint(5, 10) # Here too


	def farewell(self, bad):
		if bad == True:
			print(choice(npcFarewellBad))
			self.motivation -= randint(1, 5) # Here too
		else:
			print(choice(npcFarewell))
			self.motivation += randint(1, 5) # Here too
	
	def showStats(self):
		print('Name:', self.name)
		print('Age:', self.age)
		print('Motivation:', self.motivation)


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

	if gender == 0:
		name = choice(npcFemaleNames)
	else:
		name = choice(npcMaleNames)

	return name, age, gender, charisma, motivation

class worshipper(People):

	def __init__(self, name, age, gender, charisma, motivation, picture, newcomers_per_time, all_newcomers = 0):
		People.__init__(self, name, gender, age, picture)
		self.charisma = charisma
		self.newcomers_per_time = newcomers_per_time 
		self.all_newcomers = all_newcomers

		'''

		[charisma] - the koeficient of successful recruition (1 to 10)
		[newcomers_per_time] - the amount of people the worshipper assigns per some time (initially 1 to 10)
		[all_newcomers] - the amount of people the worshipper has ever assigned
		
		'''

	def autoRecruitment(self):
		self.all_newcomers += self.charisma * self.newcomers_per_time
		print(str(self.name) + ' has already recrited ' + str(int(self.all_newcomers)) + ' believers and has just added +' + str(self.newcomers_per_time * self.charisma))
		threading.Timer(10, self.autoRecruitment).start()

#aTutorial()

#w1 = worshipper('John', 21, 1, 7, 100, 0, 1)
#w1.autoRecruitment()