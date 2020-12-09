#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:15:39 2020

@author: charleskeenan
"""

import aocmodule as aoc

input_list = aoc.input_getter('day_3_input.txt')

day_three_part_one_solution = aoc.arboreal_collider(input_list, 1, 3)

PATHS = [(1,1),(1,3),(1,5),(1,7),(2,1)]
product = 1
for down, right in PATHS:
    trees = aoc.arboreal_collider(input_list, down, right)
    product *= trees
print(product)