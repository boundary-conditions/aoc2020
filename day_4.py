#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:25:08 2020

@author: charleskeenan
"""

import aocmodule as aoc
import re

passport_dictionary = aoc.passport_batch('day_4_input.txt')

valid_passports = 0
valid_passport_list = []
for key, value in passport_dictionary.items():
    if len(value) < 21:
        continue
    elif len(value) < 24 and 'cid' in value:
        continue
    else:
        valid_passport_list.append(value)
        valid_passports += 1
        
        
part_two = aoc.passport_batch_ver2('day_4_input.txt')

validated = 0
for key, passport in part_two.items():
    if len(passport) < 7:
        continue
    elif len(passport) < 8 and 'cid' in passport:
        continue
    else:
        for field, value in passport.items():
            valid = True
            if field == 'byr':
                if not 1920 <= int(value) <= 2002:
                    valid = False
                    #print(value)
                    break
            elif field == 'iyr':
                if not 2010 <= int(value) <= 2020:
                    valid = False
                    #print(value)
                    break
            elif field == 'eyr':
                if not 2020 <= int(value) <= 2030:
                    valid = False
                    #print(value)
                    break
            elif field == 'pid':
                if not value.isdigit() or len(value) != 9:
                    valid = False
                    #print(value)
                    break
            elif field == 'ecl':
                if value not in 'amb blu brn gry grn hzl oth':
                    valid = False
                    #print(value)
                    break
            elif field == 'hgt':
                if value[-2:] != 'cm' and value[-2:] != 'in':
                    valid = False
                    #print(value[-2:])
                    break
                elif value[-2:] == 'cm':
                    if not 150 <= int(value[:-2]) <= 193:
                        valid = False
                        #print(value)
                        break
                elif not 59 <= int(value[:-2]) <= 76:
                    valid = False
                    #print(value)
                    break
            elif field == 'hcl':
                if not bool(re.match('^#([0-9]|[a-f]){6}$', value)):
                    valid = False
                    print(value)
                    break    
            else:
                validated += 1
                break
            
                