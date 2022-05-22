#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:09:02 2022

@author: jmfustinoni
"""

import numpy as np

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    return [np.polyfit(x, y, z) for z in degs]