#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:17:39 2022

@author: jmfustinoni
"""

y = []
x = INTERVAL_1
for year in INTERVAL_1:
    y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
models = generate_models(x, y, [1])
evaluate_models_on_training(x, y, models)

# Answer
# 0.005