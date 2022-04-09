#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:27:30 2022

@author: joaomarcelofaustino
"""

"""

Next, implement the function getAvailableLetters that takes in one parameter -
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters that 
are not in lettersGuessed.

"""

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    return (''.join(sorted({letter for letter in string.ascii_lowercase if letter not in lettersGuessed})))
         
print(getAvailableLetters(lettersGuessed))