# Tutorial part

from Characters import NPC, MainCharacter
from random import randint, choice

#================================================
#				 Tutorial NPC
#================================================

npc1 = NPC('Andrew', 27, 1, 2, 50, 0)
npc2 = NPC('Bob', 32, 1, 2, 50, 1)
npc3 = NPC('Alina', 20, 0, 3, 50, 2)

#================================================
#================================================



#================================================
#				 First visit
#================================================

def FirstVisit():
	MainCharacter.greeting()
	npc1.greeting()

	while True:
		answear = input('Enter your action')

		if answear == 'q':
			answear = input('Enter your last action')
			if answear == '0':
				MainCharacter.finish_phrase(1)
				npc1.farewell(answear)

			if answear == '1':
				MainCharacter.finish_phrase(0)
				npc1.farewell(answear)
			break
		else:
			if answear == '0':
				MainCharacter.recruitment(1)
				npc1.phrase(answear)

			if answear == '1':
				MainCharacter.recruitment(0)
				npc1.phrase(answear)

	if npc1.motivation > 90:
		print('Perfect you have first member in your cult!')
	else:
		print('Damn! He\'s so strong try harder!!!')
		FirstVisit()

	
def SecondVisit():
	MainCharacter.greeting()
	npc2.greeting()

	while True:
		answear = input('Enter your action')

		if answear == 'q':
			answear = input('Enter your last action')
			if answear == '0':
				MainCharacter.finish_phrase(1)
				npc2.farewell(answear)

			if answear == '1':
				MainCharacter.finish_phrase(0)
				npc2.farewell(answear)
			break
		else:
			if answear == '0':
				MainCharacter.recruitment(1)
				npc2.phrase(answear)

			if answear == '1':
				MainCharacter.recruitment(0)
				npc2.phrase(answear)

	if npc2.motivation > 90:
		print('Perfect you have first member in your cult!')
	else:
		print('Damn! He\'s so strong try harder!!!')
		SecondVisit()



def ThirdVisit():
	MainCharacter.greeting()
	npc3.greeting()

	while True:
		answear = input('Enter your action')

		if answear == 'q':
			answear = input('Enter your last action')
			if answear == '0':
				MainCharacter.finish_phrase(1)
				npc3.farewell(answear)

			if answear == '1':
				MainCharacter.finish_phrase(0)
				npc3.farewell(answear)
			break
		else:
			if answear == '0':
				MainCharacter.recruitment(1)
				npc3.phrase(answear)

			if answear == '1':
				MainCharacter.recruitment(0)
				npc3.phrase(answear)

	if npc3.motivation > 90:
		print('Perfect you have first member in your cult!')
	else:
		print('Damn! He\'s so strong try harder!!!')
		ThirdVisit()