#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:52:45 2022

@author: jmfustinoni

Problem 6 - Playing a Game

A game consists of playing multiple hands. We need to implement one final 
function to complete our word-game program. Write the code that implements 
the playGame function. You should remove the code that is currently uncommented
in the playGame body. Read through the specification and make sure you 
understand what this function accomplishes. For the game, you should use the 
HAND_SIZE constant to determine the number of cards in a hand.

Testing: Try out this implementation as if you were playing the game. Try out 
different values for HAND_SIZE with your program, and be sure that you can play
the wordgame with different hand sizes by modifying only the variable HAND_SIZE.

Hints about the output

Be sure to inspect the above sample output carefully - very little is actually
printed out in this function specifically. Most of the printed output actually
comes from the code you wrote in playHand - be sure that your code is modular 
and uses function calls to the playHand helper function!

You should also make calls to the dealHand helper function. You shouldn't make
calls to any other helper function that we've written so far - in fact, this 
function can be written in about 15-20 lines of code.

Hopefully this hint makes the problem seem a bit more approachable.

Entering Your Code

Be sure to only paste your definition for playGame in the following box. Do not
include any other function definitions.

A Cool Trick about 'print'

A cool trick about print: you can make two or more print statements print to 
the same line! Try out the following code. It will separate the first and 
second line with a space, and the second and third line with a "?" rather than 
putting each on a new line.

print('Hello', end = " ")
print('world', end="?")
print('!')

"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    hand = ''
    
    while True:
        game = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        # inputs 'n', let the user play a new (random) hand.
        if (game == 'n'):
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        # inputs 'r', let the user play the last hand again.
        elif (game == 'r'):
            if (hand == ''):
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, HAND_SIZE)
        # inputs 'e', exit the game.
        elif (game == 'e'):
            break
        # inputs anything else, tell them their input was invalid.
        else:
            print('Invalid command.')