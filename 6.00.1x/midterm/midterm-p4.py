#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:21:52 2022

@author: jmfustinoni


Write a Python function that returns the sublist of strings in aList that 
contain fewer than 4 characters. For example, if 
aList = ["apple", "cat", "dog", "banana"], 
your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. 
Your function should not modify aList.

"""


def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    bList = []
    for i in range(len(aList)):
        if len(aList[i]) < 4:
            bList.append(aList[i])
    return bList

print(lessThan4(["apple", "cat", "dog", "banana"]))