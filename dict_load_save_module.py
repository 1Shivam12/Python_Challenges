# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:45:44 2020

@author: Shivam Bhatnagar
"""

# %%=============================================================================
# Task
## Write a function to store a dictionary into a file
# =============================================================================

# %% =============================================================================
# Imports
# =============================================================================

import pickle
import sys

# %% =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    sys.exit()

def dict_save(dic, path):
    with open(path, 'wb') as dic_file:
        pickle.dump(dic, dic_file)
        
def dict_load(path):
    with open(path, 'wb') as dic_file:
        pickle.load(dic_file)
    