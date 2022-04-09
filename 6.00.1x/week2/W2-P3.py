#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:14:41 2022

@author: joaomarcelofaustino
"""

"""

write a program that calculates the minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

"""

balance = 999999
annualInterestRate = 0.18

init_balance = balance
monthlyInterestRate = (annualInterestRate / 12.0)
lower = (init_balance / 12)
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
episilon = 0.01

while abs(balance) > episilon:
    middle = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - middle + ((balance - middle) * monthlyInterestRate)
    if balance > episilon:
        lower = middle
    elif balance < episilon:
        upper = middle
    else:
        break
print('Lowest Payment:', round(middle, 2))