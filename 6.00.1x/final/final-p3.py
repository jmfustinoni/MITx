#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:07:36 2022

@author: joaomarcelofaustino
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triangular = 0
    for num in range(1, k + 1):
        triangular += num
        if triangular == k:
            return True
    return False
    
print(is_triangular(12))
        