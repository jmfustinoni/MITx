#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:53:14 2022

@author: joaomarcelofaustino
"""

"""

Next, implement the function getGuessedWord that takes in two parameters - a 
string, secretWord, and a list of letters, lettersGuessed. This function 
returns a string that is comprised of letters and underscores, based on what 
letters in lettersGuessed are in secretWord. This shouldn't be too different 
from isWordGuessed!

"""

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    secretWord_list = []
    for letter in secretWord:
        if letter in lettersGuessed:
            secretWord_list.append(letter)
        else:
            secretWord_list.append('_ ')
        
    return(''.join(secretWord_list))
  
print(getGuessedWord(secretWord, lettersGuessed))
