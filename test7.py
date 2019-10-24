#!/bin/bash

if [ $# -eq 1 ]; then
	correct=$RANDOM
	correct=$(( correct % $1 + 1 ))
	
	guess=0
	count=0
	
	while [ $guess -ne $correct ]; do
		echo "Enter your guess no. $(( count + 1 )):"
		read guess
		
		count=$(( count + 1 ))
		
		if [ $guess -lt $correct ]; then
			echo 'too small.. try again:'
		elif [ $guess -gt $correct ]; then
			echo 'too large.. try again:'
		else 
			echo "correct guess in $count trie(s)"
		fi	
	done
	
else
	echo "Error: more than one command line arguments"
fi 

echo
echo 'thanks for playing this game!'
echo
echo 'developed/scripted by Naman R'
echo
