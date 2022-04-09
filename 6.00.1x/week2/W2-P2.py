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

balance = 3926
annualInterestRate = 0.2

def payDebt(balance, annualInterestRate,minMounthlyPayment):
    '''
    balance: int o float - the outstanding balance on the credit card
    annualInterestRate: float - annual interest rate as a decimal
    minMounthlyPayment: int - Value multiple of 10 that makes it possible to 
    pay the entire debt in 12 months
    
    returns: Debit value after 12 months paying the minimum
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    
    for i in range(1, 13):
        unpaidBalance = balance - minMounthlyPayment
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    return (round(balance, 2))
    
def findMonthyPayment(balance,annualInterestRate):
    '''
    balance: int o float - the outstanding balance on the credit card
    annualInterestRate: float - annual interest rate as a decimal
    
    returns: At the end of 12 months, lowest monthly payment that will pay off
    all debt in under 1 year
    '''
    minMounthlyPayment = 0
    while (payDebt(balance, annualInterestRate,minMounthlyPayment) >= 1):
        minMounthlyPayment += 10
    print('Lowest Payment:',minMounthlyPayment)
    
findMonthyPayment(balance, annualInterestRate)