#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 06:55:45 2022

@author: joaomarcelofaustino
"""

"""
Now you will implement the function hangman, which takes one parameter - the 
secretWord the user is to guess. This starts up an interactive game of Hangman
between the user and the computer. Be sure you take advantage of the three 
helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that
you've defined in the previous part.

"""
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    return (len({letter for letter in secretWord if letter not in lettersGuessed}) == 0)

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

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    return (''.join(sorted({letter for letter in string.ascii_lowercase if letter not in lettersGuessed})))    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord),'letters long.')
    print('-------------')
    
    guess = ''
    lettersGuessed = []
    guesses = 8
    
    while (guesses > 0):
        print('You have',guesses,'guesses left.')
        print('Available letters:',(getAvailableLetters(lettersGuessed)))
        guess = (input('Please guess a letter: ')).lower()
        lettersGuessed.append(guess)
        if (guess not in string.ascii_lowercase):
            print('Oops! You can only insert letters: ',getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        elif (lettersGuessed.count(guess) > 1):
            print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        elif (guess in secretWord):
            print('Good guess: ',getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            if (isWordGuessed(secretWord, lettersGuessed)):
                print('Congratulations, you won!')
                break
        else:
            print('Oops! That letter is not in my word: ',getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            guesses -= 1
            if (guesses == 0):
                print('Sorry, you ran out of guesses. The word was ',secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
