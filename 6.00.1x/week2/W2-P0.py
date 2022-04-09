# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!

"""

low = 0
high = 100
secret = int((high+low) / 2)
answer = ''

print('Please think a number between ' + str(low) + ' and ' + str(high) + '!')

while answer != 'c':
    print('Is your secret number ' + str(secret) + '?')
    answer = input("Enter 'h' to indicate the guess is too high. "
                   "Enter 'l' to indicate the guess is too low. "
                   "Enter 'c' to indicate I guessed correctly. ")
    if (answer == 'l'):
        low = secret
        secret = (high+low) // 2
    elif (answer == 'h'):
        high = secret
        secret = (high+low) // 2
    elif (answer == 'c'):
        break
    else:
        print("Sorry, I did not understand your input.")
    
print('Game over. Your secret number was: ' + str(secret))
