# Main file

from NPC import*
from npc_data import*
from random import randint, choice

# Creates random NPC
def createNPC():

	gender = randint(0,1)
	if gender == 1:
		name = choice(npcMaleNames)
	else:
		name = choice(npcFemaleNames)

	age = randint(18, 75)
	charisma = randint(0, 10)
	motivation = randint(0, 10)

	print(name, age, charisma, motivation)

	return name, age, gender, charisma, motivation



"""
npcList = []

for i in range(4):
	npcList.append(Person(*createNPC()))

print('Believers', Person.believers)

print(npcList)"""


