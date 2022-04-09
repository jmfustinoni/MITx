#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:51:03 2022

@author: joaomarcelofaustino

Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
    Number of times bob occurs is: 2
"""

# MyCode
s = 'azcbobobegghakl'

counter = 0
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
        counter += 1

print ('Number of times bob occurs is:', counter)

# Example
bobCount = 0

for num in range(len(s)):
    if s[num:num+3] == "bob":
        bobCount += 1
        
print("Number of times bob occurs is:", bobCount)