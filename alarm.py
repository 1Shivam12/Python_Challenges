# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:57:27 2020

@author: Shivam Bhatnagar
"""

# %%=============================================================================
# Task
## Write a python function to play a sound and print a message at a given time
# =============================================================================

# %%=============================================================================
# Imports
# =============================================================================
import datetime as dt
import time
from playsound import playsound

# %%=============================================================================
# Main
# =============================================================================


def set_alarm(al_time, sound_file, message):
    
    """
    Arguments:
        - time : a time in the form of a tuple(hh, mm, ss) 
        - sound_file : name of a sound file to play
        - message : message to print at the given time
    
    Outputs:
        - Sound file output and message  
    """
    al = True
    
    if len(al_time) < 3:
        al_time.append(0)
        target_time = al_time
    else:
        target_time = al_time
        
    while al == True:
        time.sleep(0.5)
        curr_time = dt.datetime.now()
        test_time = [curr_time.hour, curr_time.minute, curr_time.second]
        if test_time == target_time:
            print(message)
            playsound(sound_file)            
            al = False
    
    
if __name__ == "__main__":
    x = input('What time do you want to set the alarm (format: hh, mm ,ss): ')   
    time_list = x.split(',') 
    al_time = [int(x) for x in time_list]
    sound = input('What is the name of the sound file you want to play?: ')
    message = input('What is the message you want to play?: ')
    
    set_alarm(al_time, sound, message)
        