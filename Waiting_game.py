# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:26:10 2020

@author: Shivam Bhatnagar
"""

# %% Task=============================================================================
# Create a waiting game
# A random integer value of time is assigned
# The player must wait that specified amount of time and press a button
# The game will tell them how much slower or faster they were than the target time
# =============================================================================

# %% =============================================================================
# Imports
# =============================================================================
import time

import random


# %% =============================================================================
# Main
# =============================================================================


def main():
    target_time = random.randint(1,5)
    
    print(f'Your target time is {target_time} seconds')
    
    input('Press enter to begin')
    
    tic = time.perf_counter()
    
    input('Press enter to stop')
    
    toc = time.perf_counter()
    
    td = round(toc-tic,2)
    
    diff = round(abs(target_time-td),2)
    
    if td > target_time:
        print(f'Too slow! Elapsed time was {td} seconds. This was {diff} seconds too slow')
        
    elif td < target_time:
        print(f'Too fast! Elapsed time was {td} seconds. This was {diff} seconds too fast')
        
    elif td == target_time:
        print(f'Hooray! You are a master of time')
        
if __name__ == "__main__":
    main()
        






