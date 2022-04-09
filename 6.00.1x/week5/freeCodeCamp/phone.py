#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:25:11 2022

@author: jmfustinoni
"""

from item import Item

# Child class
class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity=0, broken=0):
       
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        
        # Run validation to the received arguments
        assert broken > 0, f'Broken Phones {broken} is not greater than zero!'
        
        # Assign to self object
        self.broken = broken
        