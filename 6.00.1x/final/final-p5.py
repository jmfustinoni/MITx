#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:50:29 2022

@author: joaomarcelofaustino
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """

    cryptoDict = {}
   
    for i in range(0,len(map_from)):
        cryptoDict[map_from[i]] = map_to[i]
       
    decodedWord = ""
   
    for char in code:
        decodedWord += cryptoDict[char]
     
    return cryptoDict, decodedWord

print(cipher("abcd", "dcba", "dab"))