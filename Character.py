# Main Character logic

from random import choice
from character_data import*

def greeting():
	print(choice(characterGreeting))

def recruitment():
	print(choice(characterRecruitment))

def finish_phrase():
	print(choice(characterFinishPhrase))