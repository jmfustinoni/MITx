#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 07:35:41 2022

@author: jmfustinoni

Problem 3 - Valid Words

At this point, we have written code to generate a random hand and display that
hand to the user. We can also ask the user for a word (Python's input) and 
score the word (using your getWordScore). However, at this point we have not 
written any code to verify that a word given by a player obeys the rules of 
the game. A valid word is in the word list; and it is composed entirely of 
letters from the current hand. Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you will want
to test your implementation by calling it multiple times on the same hand - 
what should the correct behavior be? Additionally, the empty string ('') is 
not a valid word - if you code this function correctly, you shouldn't need an 
additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed the 
appropriate tests in test_ps4a.py before pasting your function definition here.

"""

WORDLIST_FILENAME = "words.txt"
hand = {'p':1, 'z':1, 'u':1, 't':2, 'o':1}
word = 'tot'

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

wordList = loadWords()

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    checkHand = getFrequencyDict(word)
    
    if (word in wordList):
        for key in checkHand:
            if not ((key in hand) and (hand[key] >= checkHand[key])):
                return False
        return True
    else:
        return False
    
print(isValidWord(word, hand, wordList))
