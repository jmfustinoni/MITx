#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:43:46 2022

@author: jmfustinoni

Object Oriented Programming with Python - Full Course for Beginners
by freeCodeCamp.org
"""

# Import Parent class
from item import Item

# Add products from a CSV file
#Item.instantiate_from_csv()

#print('Item all:')
#print(Item.all)


for instance in Item.all:
    print(instance.name)

#print(item2.calculate_total_price())
#item1.apply_discount()

# See all attributes for class level
#print(Item.__dict__)

# See all attributes for instance level
#print(item1.__dict__)


