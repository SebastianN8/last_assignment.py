#
# last_assignment.py
#
# Created by: Sebastian N
# Created on: April 8
#
# This program does loops to make the user guess the actual second in the current minute

# Including time module
import time;

# My variables
guess_time = 0
local_time = time.localtime(time.time()) # This is where the exact time is stored
actual_seconds = local_time[5] # This is where just the seconds are stored

print actual_seconds

while guess_time is not actual_seconds:
	actual_seconds = local_time[5]
	guess_time = input('What do you think are the seconds past since the last change of minute: ')
	print actual_seconds
	if guess_time < 0 or guess_time > 60:
		print 'That is an invalid answer!'
	elif guess_time == actual_seconds:
		print 'You guessed the seconds!'
	elif guess_time > actual_seconds:
		print 'You might want to wait a bit to input that answer!'
	elif guess_time < actual_seconds:
		print 'You are behind the actual_time!'