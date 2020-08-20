# Tutorial part

from Characters import*
from random import randint, choice

#================================================
#				 Tutorial NPC
#================================================

npc1 = NPC('Andrew', 27, 1, 2, 90, 0)
npc2 = NPC('Bob', 32, 1, 2, 80, 1)
npc3 = NPC('Alina', 20, 0, 3, 80, 2)
npc4 = NPC('Janet', 40, 0, 5, 75, 1)
npc5 = SmartRandom(0)

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

	
