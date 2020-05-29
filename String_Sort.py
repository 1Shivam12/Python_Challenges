# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:38:45 2020

@author: Shivam Bhatnagar
"""

# %% Task =============================================================================
# Write a function to sort the words alphabetically
# =============================================================================


def string_sort(string):
    
    words = string.split(' ')
    
    word_dict = {}
    for i in words:
        word_dict[i.lower()] = i
    
    sorted_lower = sorted(word_dict.keys())
    
       
    for n, i in enumerate(sorted_lower):
        for k,v in word_dict.items():
            if i == k:
                sorted_lower[n] = v
                
          
    
    return sorted_lower


if __name__ == "__main__":
    
    x = input('Type a space separated list of words you want to sort: ')
    
    sorter = string_sort(x)
    
    print(sorter)