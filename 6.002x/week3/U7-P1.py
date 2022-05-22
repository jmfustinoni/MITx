#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:45:53 2022

@author: jmfustinoni
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if (len(L) == 0):
        return float('NaN')
    
    # compute mean first
    sumVals = 0
    for s in L:
        sumVals += len(s)
    meanVals = sumVals / len(L)

    # compute variance (average squared deviation from mean)
    sumDevSquared = 0
    for s in L:
        sumDevSquared += (len(s) - meanVals)**2
    variance = sumDevSquared / len(L)

    # standard deviation is the square root of the variance
    stdDev = variance**(.5)

    return stdDev
