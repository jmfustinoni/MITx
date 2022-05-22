#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:07:50 2022

@author: joaomarcelofaustino

As above, suppose we have a generator that returns every combination of objects
in one bag. We can represent this as a list of 1s and 0s denoting whether each
item is in the bag or not.

Write a generator that returns every arrangement of items such that each is in
one or none of two different bags. Each combination should be given as a tuple
of two lists, the first being the items in bag1, and the second being the items
in bag2.

"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """    
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)


items = [0,1]
 
print('PowerSets:')
print(list(powerSet(items)))

print('yieldAllCombos:')
print(list(yieldAllCombos(items)))