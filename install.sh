#!/bin/bash

pip install -r requirement.txt
if [[ ! -e ~/.local/bin/ToDo.py ]]; then
	cp -r ToDo.py ~/.local/bin
fi
