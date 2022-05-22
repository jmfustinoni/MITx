#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:00:44 2022

@author: joaomarcelofaustino
"""

# Generator (Fibonnaci)
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

# Memoization (Fibonnaci)
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

#for i in range(121):
#    print('fib(' + str(i) + ') =', fastFib(i))

# Generator combos
n = int(input("Enter n: "))

def truth_table_rec(n):
    if n < 1:
        return [[]]
    subtable = truth_table_rec(n-1)
    return [row + [v] for row in subtable for v in [0,1]]


def truth_table(n):
    ret = []
    for i in range(2**n):
        line = []
        for j in reversed(range(n)):
            if i//2**j % 2:
                line.append(1)
            else:
                line.append(0)
        ret.append(line)
    return ret


def truth_table_6002(n):
    ret = []
    for i in range(2 ** n):
        # print("i:", i)
        combo = []
        for j in range(n):
            if (i >> j) % 2:
                combo.append(1)
            else:
                combo.append(0)
        ret.append(combo)

    return ret


print("Recursion:")
print(truth_table_rec(n))

print("Iteration using division:")
print(truth_table(n))

print("Iteration using bitwise:")
print(truth_table_6002(n))