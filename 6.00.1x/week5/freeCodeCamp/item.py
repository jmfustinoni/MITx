#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:25:08 2022

@author: jmfustinoni
"""

import csv

# Import form child class
from phone import Phone
from tablet import Tablet
from laptop import Laptop

# Parent class
class Item:
    pay_rate = 0.8 # The pay rate afer 20% discount
    all = []
    
    def __init__(self,name,price,quantity):
        # Run validation to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
        
        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    # read only attribute
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            itemDict = list(reader)
        for item in itemDict:
            if ((item.get('product')) == 'phone'):
                Phone(
                    name=item.get('name'),
                    price = float(item.get('price')),
                    quantity=int(item.get('quantity')),
                    broken=int(item.get('broken')),
                )
            elif ((item.get('product')) == 'tablet'):
                Tablet(
                    name=item.get('name'),
                    price = float(item.get('price')),
                    quantity=int(item.get('quantity')),
                    broken=int(item.get('broken')),
                )
            elif ((item.get('product')) == 'laptop'):
                Laptop(
                    name=item.get('name'),
                    price = float(item.get('price')),
                    quantity=int(item.get('quantity')),
                    broken=int(item.get('broken')),
                )
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        
