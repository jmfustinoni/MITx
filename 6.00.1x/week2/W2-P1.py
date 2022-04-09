#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:14:41 2022

@author: joaomarcelofaustino
"""

"""

Write a program to calculate the credit card balance after one year if a 
person only pays the minimum monthly payment required by the credit card 
company each month.

For each month, calculate statements on the monthly payment and remaining 
balance. At the end of 12 months, print out the remaining balance. Be sure to
 print out no more than two decimal digits of accuracy - so print

"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def payDebt(balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: int o float - the outstanding balance on the credit card
    annualInterestRate: float annual interest rate as a decimal
    monthlyPaymentRate: float minimum monthly payment rate as a decimal
    
    returns: At the end of 12 months, print out the remaining balance
    '''
    monthlyInterestRate = annualInterestRate / 12.0

    for i in range(1, 13):
        minMounthlyPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minMounthlyPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    print("Remaining balance: ", round(balance, 2))
    
payDebt(balance, annualInterestRate, monthlyPaymentRate)