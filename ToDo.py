#! /bin/python
try:
	import questionary
	import os 
	import sys
except ImportError as e:
	print("please check that you have {} installed on your system with pip.".format(e))

todo_dir = os.path.join(os.path.expanduser('~'), '.todo')
todo_finish = os.path.join(todo_dir, 'finish.txt')
todo_todo = os.path.join(todo_dir, "todo.txt")

def date():
	import datetime
	d = datetime.datetime.now().strftime("%d")
	m = datetime.datetime.now().strftime("%m")
	h = datetime.datetime.now().strftime("%H")
	mi = datetime.datetime.now().strftime("%M")
	date = str(d+"/"+m+" "+h+":"+mi)
	return date

def verif():
	if os.path.isdir(todo_dir):
		if os.path.isfile(todo_todo):
			pass
		else:
			test = open(todo_todo, "w+")
			print(todo_todo, "is create")
			verif()
		if os.path.isfile(todo_finish):
			pass
		else:
			test1 = open(todo_finish, "w+")
			print(todo_finish, "is create")
			verif()
	else:
		os.makedirs(todo_dir)
		print(todo_dir, "is create")
		verif()

def add():
	d = date()+":> "
	task = questionary.text("[ ? ]What is the task to add at the To Do list: ").ask().capitalize()
	todo = open(todo_todo,"a+")
	todo.write(d+task+'\n')

def remove():
	d = date()+":> "
	todo = open(todo_todo, "r+")
	list1 = todo.readlines()
	todo.close()
	task = questionary.select("[ ? ]Select all the task you have finish:", list1).ask()
	list1.remove(task)
	todo = open(todo_finish, 'a+')
	todo.write(d+":: "+task)
	todo.close()
	todo = open(todo_todo, 'w+')
	k = 0
	for k in range(len(list1)):
		todo.write(list1[k])
		k = k+1
	todo.close()

def show():
    todo = open(todo_todo, 'r')
    todo = todo.readlines()
    print('-----TO DO-----')
    print(*todo)
    print('\n')
    print('----Finish-----')
    todo = open(todo_finish, 'r')
    todo = todo.readlines()
    print(*todo)
    


def main():
	main = questionary.select("[ ? ] What do you want to do with this script ?", choices=['Add', 'Finish', 'Show', 'Help']).ask()
	if main == 'Add':
		add()
	elif main == 'Finish':
		remove()
	elif main == 'Show':
		show()
	elif main == 'Help':
		print("This little script was made to maintain To Do List and have fun when i work on my TODO.\nI hope this can help you.\nUse \"Add \" or \"Finish\"")

verif()
main()
