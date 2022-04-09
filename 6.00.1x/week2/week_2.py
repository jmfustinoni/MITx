
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Write a Python function, square, that takes in one number and returns the 
square of that number.
"""

x = 5

def square(x):
    '''
    x: int or float.
    '''
    s = (x ** 2)
    return s

print(square(x))

"""
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of 
the quadratic

"""

a = 2
b = 3
c = 4
x = 5

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + b*x + c

print(evalQuadratic(a, b, c, x))

"""
Write a Python function, fourthPower, that takes in one number and returns 
that value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise 
(you don't need to redefine square in this box; when you call square, the 
 grader will use our definition).

"""
x = 2

def fourthPower(x):
    '''
    x: int or float.
    '''
    s = square(square(x))
    return s

print(fourthPower(x))

"""
Write a Python function, odd, that takes in one number and returns True when 
the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.

"""
x = 3

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return (x % 2 == 1)

print(odd(x))

"""
Write an iterative function iterPower(base, exp) that calculates the 
exponential base exp by simply using successive multiplication. 

For example, iterPower(base, exp) should compute base exp by multiplying base 
times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; 
exp will be an integer  0. It should return one numerical value. Your code 
must be iterative - use of the ** operator is not allowed.

"""

base = 4
exp = 2

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    if exp <= 0:
        return (base / base)
    else:
        for i in range(1, exp):
            result *= base
    return result

print(iterPower(base,exp))

"""
Write a function recurPower(base, exp) which compute base exp by recursively 
calling itself to solve a smaller version of the same problem, and then 
multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; 
exp will be an integer >= 0. It should return one numerical value.

Your code must be recursive - use of the ** operator or looping constructs 
is not allowed.

"""

base = 2
exp = 2

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    power = base
    if exp <= 0:
        return (base / base)
    elif exp == 1:
        return base
    else:
        return (power * recurPower((base),(exp -1)))

print(recurPower(base,exp))

"""
The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder.

Write an iterative function, gcdIter(a, b), that implements this idea. 
One easy way to do this is to begin with a test value equal to the smaller of 
the two input arguments, and iteratively reduce this test value by 1 until you 
either reach a case where the test divides both a and b without remainder, or 
you reach 1.

"""

a = 24
b = 12

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    remainder = 0;
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
        

print(gcdIter(a,b))

"""
The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder.

A clever mathematical trick (due to Euclid) makes it easy to find greatest 
common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a
Otherwise, gcd(a, b) is the same as gcd(b, a % b)

Write a function gcdRecur(a, b) that implements this idea recursively. 
This function takes in two positive integers and returns one integer.

"""

a = 12
b = 124

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
        
print(gcdRecur(a,b))

"""
We can use the idea of bisection search to determine if a character is in a 
string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're 
looking for (the "test character"). If they are the same, we are done - we've 
found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the 
middle character. If so, we need only consider the lower half of the string;
otherwise, we only consider the upper half of the string. (Note that you can 
compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea 
recursively to test if char is in aStr. char will be a single character and 
aStr will be a string that is in alphabetical order. The function should 
return a boolean value.

As you design the function, think very carefully about what the base cases 
should be.

"""

char = 'j'
aStr = 'abafgtcdefgz'

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    charL = sorted(char.lower())
    aStrL = sorted(aStr.lower())
    high = (len(aStrL))
    low = 0
    middle = (low + high) // 2
    
    if ((high <= 1) and (charL != aStrL)):
        return False
    else:
        if (charL[0] == aStrL[middle]):
            return True
        elif (charL[0] > aStrL[middle]):
            char = ''.join(charL)
            aStr = ''.join(aStrL[middle:high])
            return isIn(char,aStr)
                
        else:
            char = ''.join(charL)
            aStr = ''.join(aStrL[low:middle])
            return isIn(char,aStr)
            
print(isIn(char,aStr))

"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function
should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.

"""

n = 'j'
s = 'abafgtcdefgz'

def polysum(n, s):
    '''
    n: a positive integer (number of sides)
    s: a positive integer (length of the boundary)
    
    returns: the sum of the area and the square of the perimieter of the 
    regulary polygon, to 4 decimal spaces
    '''
    
    import math
    
    area = (0.25 * n * (s**2)) / math.tan(math.pi / n)
    perimeter = (n * s)
    
    calc = round(area + (perimeter**2),4)
    
    return calc
        
print(polysum(n,s))