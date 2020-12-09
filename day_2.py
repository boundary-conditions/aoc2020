#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:27:08 2020

@author: charleskeenan
"""

import aocmodule as aoc

input_list = aoc.input_getter('day_2_input.txt')

passwords = []
for item in input_list:
    new_password = []
    split_item = item.split(' ')
    new_password.append(split_item[0].split('-'))
    new_password[0][0], new_password[0][1] = int(new_password[0][0]), int(new_password[0][1])
    new_password.append(sum([1 for x in split_item[2] if x == split_item[1][0]]))
    # new_password.append(split_item[1][0])
    # new_password.append(split_item[2])
    passwords.append(new_password)

valid_passwords = sum([1 for x in passwords if x[1] >= x[0][0] and x[1] <= x[0][1]])
invalid_passwords = sum([1 for x in passwords if x[1] < x[0][0] or x[1] > x[0][1]])

passwords_redux = []
for item in input_list:
    new_password_redux = []
    split_item = item.split(' ')
    new_password_redux.append(split_item[0].split('-'))
    new_password_redux[0][0], new_password_redux[0][1] = int(new_password_redux[0][0])-1, int(new_password_redux[0][1])-1
    #new_password.append(sum([1 for x in split_item[2] if x == split_item[1][0]]))
    new_password_redux.append(split_item[1][0])
    new_password_redux.append(split_item[2])
    passwords_redux.append(new_password_redux)

def p_checker(item):
    low = item[0][0]
    high = item[0][1]
    string = item[2]
    letter = item[1]
    if string[low] == letter and string[high] == letter:
        return False
    elif string[low] != letter and string[high] != letter:
        return False
    else:
        return True

solution_part_two = []
for entry in passwords_redux:
    result = p_checker(entry)
    solution_part_two.append(result)
    
valid_passwords_redux = sum([1 for x in solution_part_two if x ==True])