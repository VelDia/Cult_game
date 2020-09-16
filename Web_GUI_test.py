import eel
import pickle

fileName = 'data'
fileExistsFlag = False

eel.init('web')

try:
	infile = open(fileName,'rb')
	user_info = pickle.load(infile)
	infile.close()
	print(user_info)
	fileExistsFlag = True
except IOError:
	print("Enter data please")


@eel.expose
def get_info(name, gender, age):
	if str(name) == '' or age == '':
		name = 'User'
		age = 18

	age = int(age)

	if gender == "Male":
		user_info = (str(name), age, 1)
	else:
		user_info = (str(name), age, 0)

	outfile = open(fileName,'wb')
	pickle.dump(user_info, outfile)
	outfile.close()
	
	print("Name = " + name)
	print("Gender = " + gender)
	print("Age = " + str(age))

try:
	if fileExistsFlag == True:
		eel.start('html/main.html', host='localhost', size=(500, 500))
	else:
		eel.start('html/start_page.html', host='localhost', size=(500, 500))
except:
	print("End of program")

