#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:14:33 2022

@author: jmfustinoni

Write a Python function called satisfiesF that has the specification below. 
Then make the function call run_satisfiesF(L, satisfiesF).

"""

L = ['a', 'b', 'a', 'c', 'd','a']

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    
    for i in reversed(range(len(L))):
        if f(L[i]) == False:
            L.pop(i)
    return len(L)

#run_satisfiesF(L, satisfiesF)

print(satisfiesF(L))
print(L)