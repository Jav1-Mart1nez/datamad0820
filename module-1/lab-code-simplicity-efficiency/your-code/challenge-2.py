"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import sys
import string

def RandomStringGenerator(l=12):
    
    return "".join(random.choice(string.ascii_lowercase+string.digits) for i in range(l))
   

def BatchStringGenerator(len_list, min_str=8, max_str=12):
    
    random_list = []
    for i in range(len_list):
        if min_str < max_str:
            len_strs = random.choice(range(min_str, max_str))
        elif min_str == max_str:
            len_strs = min_str
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        random_list.append(RandomStringGenerator(len_list))
    return random_list

min_str = input('Enter minimum string length: ')
max_str = input('Enter maximum string length: ')
len_list = input('How many random strings to generate? ')

print(BatchStringGenerator(int(len_list), int(min_str), int(max_str)))