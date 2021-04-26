#! /bin/python3
try:
    import os.path,sys,time,questionary
except ImportError as e:
    print(f"please check that you have {e} installed on your system with pip.")

todo_dir = os.path.join(os.path.expanduser('~'), '.todo')

todo_todo, todo_finish = os.path.join(todo_dir, "todo_todo.txt"), os.path.join(todo_dir, 'todo_finish.txt')

choices = ['Add', 'Finish', 'Show', 'Help']

file = [todo_todo, todo_finish]

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
    task = questionary.text("[ ? ] What is the task to add at the To Do list: ").ask()
    todo = open(file[0], "a+")
    todo.write(d+task+'\n')
    print("Task added:", task)

def finish():
    d = date()+":> "
    todo = open(file[0], "r+")
    list1 = todo.readlines()
    todo.close()
    task = questionary.select("[ ? ]Select all the task you have finish:", list1).ask()
    list1.remove(task)
    todo = open(file[1], 'a+')
    todo.write(d+":: "+task)
    todo.close()
    todo = open(file[0], 'w+')
    i = 0
    for i in range(len(list1)):
        todo.write(list1[i])
        i +=  1
        todo.close()

def remove():
    file_edit = questionary.select("[ ? ]Select the TODO list you want to edit:", file).ask()
    todo = open(file_edit, "r+")
    list1 = todo.readlines()
    todo.close()
    task = questionary.select("[ ? ]Select the task you want to remove:", list1).ask()
    list1.remove(task)
    list1 = ('\n').join(list1)
    todo = open(file_edit, 'w+')
    todo.write(list1)
    todo.close()
    os.system(f"sed '/^[[:space:]]*$/d' {file_edit} > /tmp/todo_swap && cat /tmp/todo_swap > {file_edit}")

def show():
    i=0
    for i in range(len(file)):
        title = [ "TODO on going", "TODO FINISH"]
        todo = open(file[i], 'r')
        todo = todo.readlines()
        todo = ('').join(todo)
        title = title[i]
        print(f"{title}:\n{todo}")

def main():
    if len(sys.argv) == 1:
        print("Use \"Add \", \"Finish\", \"Show\", \"Remove\"")
    else:
        arg = sys.argv[1].capitalize()
        if arg == "Add":
            print("Do you want to add task ? :[Yes/no]")
            yn=input().capitalize()
            while yn:
                if yn == "Yes" or yn == "Y":
                    add()
                    print("Do you want to add task again ? :[Yes/no]")
                    yn=input().capitalize()
                elif yn == "No" or yn == "N":
                    print("Good bye")
                    yn=None
                else:
                    print("Do you want to add task again ? :[Yes/no]")
                    yn=input().capitalize()
        elif arg == "Finish":
            print("Do you want to set task as finish ? :[Yes/no]")
            yn=input().capitalize()
            while yn:
                if yn == "Yes" or yn == "Y":
                    finish()
                    print("Do you want to set task as finish ? :[Yes/no]")
                    yn=input().capitalize()
                elif yn == "No" or yn == "N":
                    print("Good bye")
                    yn=None
                else:
                    print("Do you want to set task as finish ? :[Yes/no]")
                    yn=input().capitalize()
        elif arg == "Show":
            show()
        elif arg == "Remove":
            print("Do you want to remove task ? :[Yes/no]")
            yn=input().capitalize()
            print(yn)
            while yn:
                if yn == "Yes" or yn == "Y":
                    remove()
                    print("Do you want to remove task again ? :[Yes/no]")
                    yn=input().capitalize()
                elif yn == "No" or yn == "N":
                    print("Good bye")
                    yn=None
                else:
                    print("Do you want to remove task again ? :[Yes/no]")
                    yn=input().capitalize()
                    print(yn)
                else:
                    print("This little script was made to maintain To Do List and have fun when i work on my TODO.\nI hope this can help you:\n\tDo it: Do it Now \n\tDecide: Schedule a time to do it \n\tDelegate: Who can do it for you \n\tDelete: remove that task or do it when you are boring.\nUse \"Add \", \"Finish\", \"Show\", \"Remove\"")

verif()
main()
