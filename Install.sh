export $PATH: ~/.local/bin/

sudo pip install -G -r requirement.txt

printf "[+] Create .ToDo"
mkdir ~/.ToDo/
printf "[+] Create todo.txt"
touch ~/.ToDo/todo.txt
printf "[+] Create finish.txt"
touch ~/.ToDo/finish.txt

printf "All is done. Exiting the script "