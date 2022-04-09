#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:31:18 2022

@author: joaomarcelofaustino

Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
"""

s = 'azcbobobegghakl'
vCount = 0

for vowel in s:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        vCount += 1

print('Number of vowels: ' + str(vCount))