#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:53:14 2022

@author: joaomarcelofaustino
"""

"""

First, implement the function isWordGuessed that takes in two parameters - a 
string, secretWord, and a list of letters, lettersGuessed. This function 
returns a boolean - True if secretWord has been guessed (ie, all the letters 
of secretWord are in lettersGuessed) and False otherwise.

"""

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    return (len({letter for letter in secretWord if letter not in lettersGuessed}) == 0)
    
print(isWordGuessed(secretWord, lettersGuessed))
