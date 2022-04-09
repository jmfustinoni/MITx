#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:41:42 2022

@author: jmfustinoni
"""
# Problem 6
# 15/15 points (graded)
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList 
#    '''
  


# Paste your function here
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    newList = []
    for item in aList:
        if type(item) != type([]):
            newList.append(item)
        else:
            newList.extend(flatten(item))
    return newList

# Correct


print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
