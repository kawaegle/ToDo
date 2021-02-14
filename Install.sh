#!/bin/sh

pip3 install -r requirement.txt

printf "[+] Create .ToDo\n"
mkdir -p ~/.ToDo/
printf "[+] Create todo_urgent.txt\n"
touch ~/.ToDo/todo_urgent.txt
printf "[+] Create todo_decide.txt\n"
touch ~/.ToDo/todo_decide.txt
printf "[+] Create delegate.txt\n"
touch ~/.ToDo/todo_delegate.txt
printf "[+] Create finish.txt\n"
touch ~/.ToDo/finish.txt

printf "All is done. Exiting the script\n"