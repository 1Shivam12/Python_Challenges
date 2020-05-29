# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:50:17 2020

@author: Shivam Bhatnagar
"""

# %% Task=============================================================================
# Find indices for all items in a list equal to a given value
# =============================================================================


def find_all(listo, val):
    
    """
    Purpose: Function that returns all indices of a given value in a list
    
    Inputs:
        - listo : list containing the values we want to index
        - val : the value whose index we want to find
        
    Outputs:
        - inds : list of indices
    """
    # Expected out : inds = [[0,1],2,[3,2]]

    inds = []
    
    for i in range(len(listo)):
        if listo[i] == val:
            inds.append([i])
        elif type(listo[i]) == list:
            for ind in find_all(listo[i], val):
                inds.append([i]+ind)
    
    return inds


if __name__ == "__main__":
    
    x = input('What is the list you want to pass in?: ')
    y = input('What is the target value you want to find?: ')
    
    inds = find_all(x,y)
    
    print(inds)
                    
            
        
  
        
 