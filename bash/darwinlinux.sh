#!/bin/bash
# Detect if the script is running on Darwin (MacOS) or Linux operating system
if [ "$(uname)" == "Darwin" ]; then
	echo "It's a Mac";
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
	echo "It's Linux"
fi
