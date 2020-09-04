import eel
eel.init('web')

@eel.expose
def get_info(name, gender, age):
	print("Name = " + str(name))
	print("Gender = " + str(gender))
	print("Age = " + str(age))

try:
	eel.start('html/start_page.html', host='localhost', size=(500, 500))
except:
	print("End of program")

