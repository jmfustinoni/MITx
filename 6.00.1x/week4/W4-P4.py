#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 08:58:59 2022

@author: jmfustinoni

Problem 4 - Hand Length

We are now ready to begin writing the code that interacts with the player. 
We'll be implementing the playHand function. This function allows the user to 
play out a single hand. First, though, you'll need to implement the helper 
calculateHandlen function, which can be done in under five lines of code.

"""
hand = {'p':1, 'z':1, 'u':1, 't':2, 'o':1}

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLen = 0
    for key in hand:
        handLen += hand[key]
    return(handLen)

print(calculateHandlen(hand))