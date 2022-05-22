#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:53:27 2022

@author: jmfustinoni
"""

import random

# helper function

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return (mean, std)  
  
def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for 
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess
    
    Runs a Monte Carlo simulation, 'num_trials' times. In each trial 
    you guess what each food is, the ith food has 'prob[i]' probability 
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars. 
    
    Returns: a tuple of the mean and standard deviation over 
    'num_trials' trials of the net money earned 
    when making len(probs) guesses
    """
    money=[]
    moneyEarned = 0.0
    s = 0.0
    quantity = len(probs)
    for i in range(num_trials):
        moneyEarned = 0.0
        for n in range(quantity):
            if probs[n] == 1:
                moneyEarned += (1*get) - (1*cost)
            elif probs[n] == 0:
                moneyEarned += -1*cost
            else:    
                s = random.betavariate(probs[n], 1-probs[n])
                moneyEarned += s* get -n*cost    
        money.append(moneyEarned)
       
    return(getMeanAndStd(money))    
        
print(guessfood_sim(100, [1, 1, 1], 1, 0))        
(-3.0, 0.0)    