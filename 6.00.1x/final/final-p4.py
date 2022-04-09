#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:07:36 2022

@author: joaomarcelofaustino
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    temp = set(L)
    while len(temp) > 0:
        largest = max(temp)
        if (L.count(largest) % 2) != 0:
            return largest
        else:
            temp.remove(largest)

print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,3,5,3]))