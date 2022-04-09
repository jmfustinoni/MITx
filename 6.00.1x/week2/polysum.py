#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:33:22 2022

@author: jmfustinoni
"""

def polysum(n, s):
    '''
    n: a positive integer (number of sides)
    s: a positive integer (length of the boundary)
    
    returns: the sum of the area and the square of the perimieter of the 
    regulary polygon, with 4 decimal spaces
    '''
    
    import math
    
    area = (0.25 * n * (s**2)) / math.tan(math.pi / n)
    perimeter = (n * s)
    
    return round(area + (perimeter**2),4)
