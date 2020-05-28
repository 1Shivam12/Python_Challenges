# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:53:03 2020

@author: Shivam Bhatnagar
"""

# %% Task =====================================================================
# Write a function to return prime factors of a given integer
# =============================================================================

# %% ==========================================================================
# Imports
# =============================================================================



# %%  =========================================================================
# Function
# =============================================================================

   
def get_primes(num):
    
    
    """
    Purpose : Function that returns prime factors of the input integer
    
    
    Arguments :
        
        - num : integer
        
    Output :
        
        - prime_facs : list containing the prime factors
    
    """   
    prime_facs = []

    orig_num = num
    
    def is_prime(x):
        if x > 1:
            for i in range(2, x):
                if not x % i:
                    return False
        else:
            return False
        
                        
        return True
    
    def get_lowest_prime_fac(y):
        
        div = 2
        while True:
                        
            if (y % div == 0) and (is_prime(div) == True):
                
                lpf = div
                return lpf
            else:
                div += 1
                
                
        
                
    flag = True
    counter = 1
    next_div = 0
    while flag == True:
        if counter == 1:
            start_div = orig_num
        else:
            start_div = next_div
        
        
        lpf = get_lowest_prime_fac(start_div)
        
        prime_facs.append(lpf)
        next_div = start_div / lpf
        counter += 1
        if next_div == 1:
            flag = False
        
        
    return prime_facs
        
            

    
if __name__ == "__main__":
    x = int(input('What number do you want to test?: '))
    prime_facs = get_primes(x)
    print(prime_facs)

