#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:28:31 2022

@author: joaomarcelofaustino

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print:
    Longest substring in alphabetical order is: beggh    
"""


s = 'azcbobobegghakl'
alpha = s[0]
longest = s[0]

for x in range(len(s)-1):
    y = (len(alpha)-1)
    if alpha[y] <= s[x+1]:
        alpha = alpha + s[x+1]
        if len(alpha) > len(longest):
            longest = alpha   
    else:
        alpha = s[x+1]
        if len(alpha) > len(longest):
            longest = alpha
print("Longest substring in alphabetical order is:",longest)