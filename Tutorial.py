# Tutorial part

from Characters import People, NPC, MainCharacter, Character
from character_data import*
#from random import randint, choice

#================================================
#				 Tutorial NPC
#================================================

npc1 = NPC('Andrew', 27, 1, 50, 0)
npc2 = NPC('Bob', 32, 1, 50, 0)
npc3 = NPC('Alina', 20, 0, 50, 0)

#================================================
#================================================



#================================================
#				 First visit
#================================================
'''
def FirstVisit():
	MainCharacter.greeting()
	npc1.greeting()

	while True:
		answear = bool(input('Enter your action'))

		if answear == 'q':
			answear = input('Enter your last action')
			if answear == '0':
				MainCharacter.finish_phrase(True)
				npc1.farewell(answear)

			if answear == '1':
				MainCharacter.finish_phrase(False)
				npc1.farewell(answear)
			break
		else:
			if answear == '0':
				MainCharacter.recruitment(True)
				npc1.phrase(answear)

			if answear == '1':
				MainCharacter.recruitment(False)
				npc1.phrase(answear)

	if npc1.motivation > 90:
		print('Perfect you have first member in your cult!')
	else:
		print('Damn! He\'s so strong try harder!!!')
		#FirstVisit()
'''

def Visit():
	MainCharacter.greeting()
	npc1.greeting()
	npc1.showStats()
	#bool bad1 = False, bad2 = False, bad3 = False
	bad1 = MainCharacter.recruitment(characterRecruitmentSoft,characterRecruitmentSoftBad, bad1)
	npc1.phrase(bad1)
	npc1.showStats()
	bad2 = MainCharacter.recruitment(characterRecruitmentHard, characterRecruitmentHardBad, bad2)
	npc1.phrase(bad2)
	npc1.showStats()
	bad3 = MainCharacter.recruitment(characterFinishPhrase, characterFinishPhraseBad, bad3)
	npc1.farewell(bad3)
	npc1.showStats()
	if npc1.motivation <= 50:
		print('You lost... The person didn`t believe you.')
	elif npc1.motivation > 50 and npc1.motivation < 90:
		print('Congrats, you`ve got a new believer.')
		MainCharacter.add_believer()
	elif npc1.motivation >= 90:
		print('Heh, you were good enough to get a worshipper.')
		MainCharacter.add_believer()
	print('The amount of believers:', MainCharacter.believers)
		
'''
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

'''

Visit()