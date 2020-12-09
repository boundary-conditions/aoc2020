#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 06:13:56 2020

@author: charleskeenan
"""

# def input_collector():
#     numbers = []
#     while True:
#         thing = input()
#         if len(thing) == 0:
#             break
#         numbers.append(thing)
#     return numbers

# Get input from text file, read in to list
def input_getter(filename, option='r'):
    input_list = []
    with open(filename, option) as code_input:
        for line in code_input:
            input_list.append(line.rstrip())
    return input_list


def arboreal_collider(lst, down, right):
    row, col = 0, 0
    TOTAL_ROWS = len(lst) - 1
    TOTAL_COLUMNS = len(lst[0])
    trees = 0
    while row < TOTAL_ROWS:
        row += down
        col = (col + right) % TOTAL_COLUMNS
        if lst[row][col] == '#':
            trees += 1
    return trees

def passport_batch(filename, option='r'):
    passport_dictionary = {}
    count = 1
    with open(filename, option) as pp:
        for line in pp:
            if len(line) < 3:
                count += 1
            first_split = line.split(' ')
            new_line = []
            for item in first_split:
                item = item.split(':')
                new_line.append(item[0])
            for item in new_line:
                passport_dictionary[count] = passport_dictionary.get(count, "") + item
    return passport_dictionary

def passport_batch_ver2(filename, option='r'):
    passport_dictionary = {}
    count = 1
    with open(filename, option) as pp:
        for line in pp:
            if len(line) < 3:
                count += 1
                continue
            first_split = line.split(' ')
            new_dict = {}
            for item in first_split:
                items = item.split(':')
                
                new_dict[items[0]] = items[1].strip()
            passport_dictionary[count] = passport_dictionary.get(count, {})
            passport_dictionary[count].update(new_dict)
    return passport_dictionary
        