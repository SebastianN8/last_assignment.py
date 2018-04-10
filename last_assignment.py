#
# last_assignment.py
#
# Created by: Sebastian N
# Created on: April 8
#
# This program does loops to make the user guess the actual second in the current minute

import time

# My variables
guess_time = 0
guess_time_number = int(guess_time)
local_time = time.localtime(time.time()) # This is where the exact time is stored
actual_seconds = local_time[5] # This is where just the seconds are stored

while (guess_time_number is not actual_seconds):
    local_time = time.localtime(time.time()) # This is where the exact time is stored
    actual_seconds = local_time[5] # This is where just the seconds are stored
    guess_time = input('What do you think are the seconds past since the last change of minute: ')
    guess_time_number = int(guess_time)
    if guess_time_number < 0 or guess_time_number > 60:
        print('That is an invalid answer!')
    elif guess_time_number == actual_seconds:
		    print('You guessed the seconds!')
    elif guess_time_number > actual_seconds:
        print('You might want to wait a bit to input that answer!')
    elif guess_time_number < actual_seconds:
        print('You are behind the actual_time!')
    else:
		    print('Invalid answer!')

input()