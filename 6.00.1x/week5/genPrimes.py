#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:32:10 2022

@author: jmfustinoni
"""

# Generator
def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

# Function            
def genPrimesFn():
    '''Function to keep printing the prime number until the user stops the program.
    This way uses user input; you can also just run an infinite loop (while True)
    that the user can quit out of by hitting control-c'''
    primes = []   # primes generated so far
    last = 1      # last number tried
    uinp = 'y'    # Assume we want to at least print the first prime...
    while uinp != 'n':
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            print(last)
            uinp = input("Print the next prime? [y/n] ")
            while uinp != 'y' and uinp != 'n':
                print("Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no.")
                uinp = input("Print the next prime? [y/n] ")