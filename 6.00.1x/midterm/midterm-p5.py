#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:33:13 2022

@author: jmfustinoni

Write a Python function that returns a list of keys in aDict that map to 
integer values that are unique (i.e. values appear exactly once in aDict). 
The list of keys you return should be sorted in increasing order. 
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    
    keyList = []
    keyDict = {}

    for key in list(aDict.keys()):
        if aDict[key] not in keyDict:
            keyDict[aDict[key]] = 1
        else:
            keyDict[aDict[key]] += 1

    for keyInkeyDict in keyDict.keys():
        if keyDict[keyInkeyDict] == 1:
            for keyInaDict in aDict.keys():
                if aDict[keyInaDict] == keyInkeyDict:
                    keyList.append(keyInaDict)

    return sorted(keyList)

aDict = {1: 1, 2: 3, 3: 2, 4:3}

print(uniqueValues(aDict))