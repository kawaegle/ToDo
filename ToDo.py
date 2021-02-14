#! /bin/python
try:
	import os.path
	import sys
	from rofi import Rofi
	import time
	import notify
except ImportError as e:
	print(f"please check that you have {e} installed on your system with pip.")

todo_dir = os.path.join(os.path.expanduser('~'), '.todo')

todo_todo, todo_finish = os.path.join(todo_dir, "todo_todo.txt"), os.path.join(todo_dir, 'todo_finish.txt')

choices = ['Add', 'Finish', 'Show', 'Help']
file = [todo_todo, todo_finish]

r = Rofi()

def date():
	from datetime import datetime
	d, m, h, mi = datetime.now().strftime("%d"), datetime.now().strftime("%m"), datetime.now().strftime("%H"), datetime.now().strftime("%M")
	date = str(d+"/"+m+" "+h+":"+mi)
	return date

def verif():
	if os.path.isdir(todo_dir):
		i= 0
		for i in range(len(file)):
			if os.path.isfile(file[i]):
				pass
			else:
				open(file[i], "w+")
				print("create", file[i])
				verif()
				i += 1
	else:
		os.makedirs(todo_dir)
		print(todo_dir, "is create")
		verif()

def add():
	d = date()+":> "

	task = r.text_entry("[ ? ] What is the task to add at the To Do list: ")
	todo = open(file[0],"a+")
	todo.write(d+task+'\n')
	notify.notification_total("TODO add", task)

def finish():
	d = date()+":> "
	todo = open(file[0], "r+")
	list1 = todo.readlines()
	todo.close()
	task = r.select("[ ? ]Select all the task you have finish:", list1)
	task = list1.pop(task[0])
	notify.notification_total("TODO finish", task)
	todo = open(file[1], 'a+')
	todo.write(d+":: "+task+"\n")
	todo.close()
	todo = open(file[0], 'w+')
	i = 0
	for i in range(len(list1)):
		todo.write(list1[i])
		i +=  1
	todo.close()

def show():
	i=0
	for i in range(len(file)):
		data = [ "TODO on going", "TODO FINISH"]
		todo = open(file[i], 'r')
		todo = todo.readlines()
		title = data[i]
		notify.notification_total(title, todo)
		time.sleep(5)

def main():
	arg = sys.argv[1]
	if arg == "add":
		add()
	elif arg == "finish":
		finish()
	elif arg == "show":
		show()
	else:
		notify.notification_desc("This little script was made to maintain To Do List and have fun when i work on my TODO.\nI hope this can help you.")
		time.sleep(5)
		notify.notification_desc("\n\tDo it: Do it Now \n\tDecide: Schedule a time to do it \n\tDelegate: Who can do it for you \n\tDelete: remove that task or do it when you are boring")
		time.sleep(5)
		notify.notification_desc("Use \"Add \", \"Finish\", \"Show\"")


verif()
main()