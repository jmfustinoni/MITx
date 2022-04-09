#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:53:04 2022

@author: jmfustinoni

Problem 2 - Dealing with Hands

Representing hands

Removing letters from a hand

The player starts with a hand, a set of letters. As the player spells out 
words, letters from this set are used up. For example, the player could start 
out with the following hand: a, q, l, m, u, i, l. The player could choose to 
spell the word quail . This would leave the following letters in the player's 
hand: l, m. Your task is to implement the function updateHand, which takes in 
two inputs - a hand and a word (string). updateHand uses letters from the hand
to spell the word, and then returns a copy of the hand, containing only the 
letters remaining. For example:

>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
>>> displayHand(hand) # Implemented for you
a q l l m u i
>>> hand = updateHand(hand, 'quail') # You implement this function!
>>> hand
{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
>>> displayHand(hand)
l m  
Implement the updateHand function. Make sure this function has no side effects:
i.e., it must not mutate the hand passed in. Before pasting your function 
definition here, be sure you've passed the appropriate tests in test_ps4a.py.

Hints
Testing

Testing: Make sure the test_updateHand() tests pass. You will also want to test
your implementation of updateHand with some reasonable inputs.

Copying Dictionaries

You may wish to review the ".copy" method of Python dictionaries 
(review this and other Python dictionary methods here).


Your implementation of updateHand should be short (ours is 4 lines of code). 
It does not need to call any helper functions.

"""

hand = {'p':1, 'z':1, 'u':1, 't':3, 'o':1}
word = 'tot'
hand.get('t',0)

print('Hand = ',hand)

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()

displayHand(hand)
print('word = ',word)

def getFrequencyDict(word):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in word:
        freq[x] = freq.get(x,0) + 1
    return freq

print('Frequency = ', getFrequencyDict(word))

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for letter in word:
        if (newHand.get(letter,0) > 1):
            newHand[letter] -= 1
        else:
            del newHand[letter]
    return newHand
            
            

print(updateHand(hand, word))
    