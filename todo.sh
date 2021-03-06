#!/bin/bash

# Options
Add="add a task"
Finish="set a task as finish"
Show="show all task"
Help="show help"

# Variable passed to rofi
options="$Add\n$Finish\n$Show\n$Help"
chosen="$(echo -e "$options" | rofi -dmenu)"

case $chosen in
    $Add)
        python3 ToDo.py add
        ;;
    $Finish)
        python3 ToDo.py finish
        ;;
    $Show)
        python3 ToDo.py show
        ;;
    $Help)
        python3 ToDo.py help
        ;;
esac