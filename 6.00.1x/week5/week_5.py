#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 09:28:12 2022

@author: jmfustinoni
"""

# Example of OOP
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff = (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        return (x_diff + y_diff) *0.5
    def __str__(self):
        return "<" + str(self.x) + ","  + str(self.y) + ">"

A = Coordinate(3,5)
B = Coordinate(10,6)
print(A)
print(B)
print(A.distance(B))


# Exercise Coordinates

"""
Your task is to define the following two methods for the Coordinate class:

Add an __eq__ method that returns True if coordinates refer to same point in 
the plane (i.e., have the same x and y coordinate).

Define __repr__, a special method that returns a string that looks like a valid
Python expression that could be used to recreate an object with the same value.
In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self,other):
        # Compare if oordinates refer to same point in the plane
        if ((self.x == other.x)and(self.y == other.y)):
            return True
        else:
            return False
        
    def __repr__(self):
        # Recreate an object with the same value
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'
    

# Exercise int set

"""
Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements that 
appear in both sets. In other words,

s1.intersect(s2)

would return a new intSet of integers that appear in both s1 and s2. 
Think carefully - what should happen if s1 and s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of elements in 
s.
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
   
        guess = intSet()
        for val in self.vals:  
            if other.member(val):
                guess.insert(val)
        return guess
    
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """Return number of integers in self"""
        return len(self.vals)
    
# Exercise spell
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)


print(Accio())
