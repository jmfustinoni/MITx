#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:25:21 2022

@author: jmfustinoni
"""

# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
# MISSING LINES
models = generate_models(x1, y, [1])    
evaluate_models_on_training(x1, y, models)

"""
Problem 4.1
"""

# Answer
for year in INTERVAL_1:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', year)))
    

"""
Problem 4.2
"""

# Answer
0.085