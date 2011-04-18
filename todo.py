#!/usr/bin/python2
###############################################################################
# Task list
# @author: randynobx@gmail.com

# Task elements: Desc, Status, Priority
###############################################################################
import os
import sys
import re
import io

def help_message():
	print '''Task List -- tracks your todo list
Options: -l		-- lists all existing tasks
	 -n [new task]	-- adds a new task to the todo list
	 -m [task id]	-- marks a task complete
	 -e [task id] [new task] -- edits an existing task
	 -C		-- clears the list
	 -h		-- displays this help message
	 -V		-- displays version of Task List'''
	sys.exit(0)
def version_message():
	print '''Task List v0.2
Last Modified: 00:02:06 14/04/2011 
By Randy Nance [randynobx@gmail.com]'''
def print_list():
	# List all tasks
	print 'To-do List Manager'
	print '----------------------------------'
	with open(path,'r') as file:
		i = int(file.read(1))
		if i > 0:
			for line in file:
				result = re.match(' Items', line)
				if result == None:
					print line
		elif i == 0:
			print 'There are no tasks to be completed.'
	print '----------------------------------'

def check_empty():
	with open(path,'r') as file:
		if int(file.read(1)) == 0:
			print 'There are no tasks to be completed.'
			sys.exit(0)

# File path to todo txt file
path = "/home/randy/Documents/todo_list.txt"

if len(sys.argv) == 1: # Default message
	version_message()
	help_message()
	sys.exit(0)
if sys.argv[1] == '-h':
	help_message()
if sys.argv[1] == '-V':
	version_message()
if sys.argv[1] == '-l':
	# List all tasks
	print_list()
	sys.exit(0)
if sys.argv[1] == '-n' and sys.argv[2] != '':
	# Create new task
	nt = " ".join(sys.argv[2:])
	with open(path,'r') as file:
		id = int(file.read(1)) # Get id for new task
		tk = file.readlines()
	if id == 0:
		id += 1
	nxtid = len(tk) + 1
	with open(path,'w') as file:
		file.write(str(nxtid))
		for t in tk:
			file.write(t)
		file.write(str(id) + '\t' + nt + '\n')
	sys.exit(0)
elif sys.argv[1] == '-n' and sys.argv[2] == '':
	print '-n expects an argument'
	sys.exit(0)
if sys.argv[1] == '-e' and sys.argv[2] != '' and sys.argv[3] != '': #Edit task with given id
	# Edit task
	check_empty()
	id = int(sys.argv[2])
	new = " ".join(sys.argv[3:])
	if id <= 0:
		print 'not a valid id. id must be greater than 0'
		sys.exit(0)
	with open(path,'r') as file:
		tk = file.readlines()
	with open(path,'w') as file:
		for t in tk:
			result = re.match(str(id) + '\t.*',t)
			if result:
				file.write(str(id) + '\t' + new + '\n')
			else:
				file.write(t)
elif sys.argv[1] == '-e' and sys.argv[2] == '':
	print '-e expects 2 arguments'
	sys.exit(0)
if sys.argv[1] == '-m' and sys.argv[2] != '':
	# Mark [delete] specified task complete
	d = sys.argv[2]
	if d < 1: # Check for valid id
		print 'not a valid id. id must be greater than 0'
		sys.exit(0)
	check_empty() # Check for empty list
	id = d #id of next added task will replace the last marked task
	with open(path,'r') as file:
		file.read(1) # Keep header out of task output
		tk = file.readlines()
	with open(path,'w') as file:
		file.write(id)
		for t in tk:
			result = re.match(d + ".*$",t)
			if result == None:
				file.write(t)
	sys.exit(0)
elif sys.argv[1] == '-m' and sys.argv[2] == '':
	print '-m expectd an argument'
	sys.exit(0)
	
if sys.argv[1] == '-C':
	result = raw_input('Are you sure you want to clear your todo list? y/n: ')
	if result == 'y' or result == 'Y' or result == 'yes' or result == 'Yes':
		with open(path,'w') as file:
			file.write('0 Items\n')
		
if sys.argv[1] == '-s': #sort
	print 'sort function'
	sys.exit(0)
#TESTING PURPOSES ONLY
if sys.argv[1] == '-t':
	with open(path,'r') as file:
		print file.read(1)
	sys.exit(0)
