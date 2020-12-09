#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:47:36 2020

@author: charleskeenan
"""

import aocmodule as aoc

puzzle_input = aoc.input_getter('day_6_input.txt')

group_list = []
group = []
for i in range(len(puzzle_input)):
    if len(puzzle_input[i]) == 0:
        group_list.append(group)
        group = []
        continue
    group.append(puzzle_input[i])
group_list.append(group)
    


def letter_checker(a,b):
    both = [x for x in a if x in b]
    both_string = ''.join(both)
    return both_string

logs2 = []    
for g in group_list:
    group_size = len(g)
    final_string = g[0]
    for i in range(group_size):
        like_string = letter_checker(final_string, g[i])
        final_string = like_string
        all_yes = final_string
                           
    logs2.append(all_yes)
    
second_count = 0
for item in logs2:
    i = len(item)
    second_count += i


print(sum([len(set.intersection(*[set(j) for j in i.split()])) for i in open('day_6_input.txt').read().split('\n\n')]))
# for i in item:
#     s = [x for x in i if x not in new_item]
#     try:
#         new_item = new_item + ''.join(s)
#     except:
#         new_item = new_item


# group_string = ''
# list_of_group_strings = []
# for person in puzzle_input:
#     if len(person) == 0:
#         list_of_group_strings.append(group_string)
#         group_string = ''
#     for response in person:
#         s = [ltr for ltr in response if ltr not in group_string]
#         try:
#             group_string = group_string + ''.join(s)
#         except:
#             group_string = group_string
# list_of_group_strings.append(group_string)           

# count = 0
# for item in list_of_group_strings:
#     i = len(item)
#     count += i
    
    
    

