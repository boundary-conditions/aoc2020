#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:47:15 2020

@author: charleskeenan
"""

import aocmodule as aoc

puzzle_input = aoc.input_getter('day_5_input.txt')

def row_reducter(x, lst): #x is F or B from boarding pass, lst is a list of integers
    lst_length = len(lst)
    if x == 'B' or x == 'R':
        lst = lst[int((lst_length / 2)):]  
    elif x =='F' or x == 'L':
        lst = lst[:int((lst_length / 2))]
    return lst

highest_id = 0

for bp in puzzle_input:
    rows = [x for x in range(128)]
    cols = [x for x in range(8)]
    for i in range(7):
        rows = row_reducter(bp[i], rows)
    for j in range(7,10):
        cols = row_reducter(bp[j], cols)
    pass_value = (rows[0] * 8) + cols[0]
    if pass_value > highest_id:
        highest_id = pass_value
        
all_passes = []       
for bp in puzzle_input:
    rows = [x for x in range(128)]
    cols = [x for x in range(8)]
    for i in range(7):
        rows = row_reducter(bp[i], rows)
    for j in range(7,10):
        cols = row_reducter(bp[j], cols)
    pass_value = (rows[0] * 8) + cols[0]
    all_passes.append(pass_value)

all_passes.sort()
for x in range(1, 907):    
    if all_passes[x] - all_passes[x-1] == 2:
        my_seat = all_passes[x]-1



