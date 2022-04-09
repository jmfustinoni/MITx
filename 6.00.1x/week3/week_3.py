#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:02:16 2022

@author: jmfustinoni
"""

"""

For each of the following questions (which you may assume is evaluated 
independently of the previous questions, so that testList has the value 
indicated above), provide an expression using applyToEach, so that after 
evaluation testList has the indicated value. You may need to write a simple 
procedure in each question to help with this process.

"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# Exercise 1
# [1, 4, 8, 9]

testList = [1, -4, 8, -9]
print('Exercise 1:',testList)

applyToEach(testList, abs)

print(testList)

# Exercise 2
#[2, -3, 9, -8]

testList = [1, -4, 8, -9]
print('Exercise 2:',testList)

def increaseList(L):
    return (L + 1)

applyToEach(testList, increaseList)

print(testList)

# Exercise 3
# [1, 16, 64, 81]

testList = [1, -4, 8, -9]
print('Exercise 3:',testList)

def quadList(L):
    return (abs(L)**2)

applyToEach(testList, quadList)

print(testList)

"""
Here is a different piece of code for working with lists:
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

"""
Suppose that you are given the following functions:
"""

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))

print(applyEachTo([inc, square, halve, abs], 3.0))

#print(applyEachTo([inc, max, int], -3))
#error

# Execise 4

"""
First, write a procedure, called how_many, which returns the sum of the number 
of values associated with a dictionary.
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    many = 0
    for n in aDict:
        many = many + (len(aDict[n]))
    return many
        
print(how_many(animals))

# Execise 5

"""
write a procedure, called biggest, which returns the key corresponding to the 
entry with the largest number of values associated with it. If there is more 
than one such entry, return any one of the matching keys
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    bigKey = ''
    bigValue = 0
    for n in aDict:
        if (len(aDict[n]) >= bigValue):
            bigKey = n
            bigValue = len(aDict[n])
    return bigKey
        
print(biggest(animals))
        














