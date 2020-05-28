# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:23:47 2020

@author: Shivam Bhatnagar
"""

# %% Task =============================================================================
# Check if a given string is a palindrome
# =============================================================================


# %% =============================================================================
# Implementation
# =============================================================================

def is_palindrome(string):
    text = ''
    string = string.lower()
    for i in string:
        if i.isalpha():
            text += i
    
    if text ==  text[::-1]:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    
    x = input('Type the string you want to check: ' )
    flag = is_palindrome(x)
    
    if flag == True:
        print(f'{x} is a palindrome')
    else:
        print(f'{x} is not a palindrome')