#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:35:30 2020

@author: charleskeenan
"""

import re

rule_pat = re.compile(r'(\d+) ([a-z ]+) bag')

with open('day_7_input.txt', 'r') as f:
    rules = {}
    # Read the rules
    for l in f:
        data = l.split(' ', 4)
        container = ' '.join(data[0:2])
        rules[container] = [(item[1], int(item[0])) for item in rule_pat.findall(data[-1])]
    # Work out how many bags inside
    buffer = rules['shiny gold'].copy()
    count = 0
    for bag in buffer:
        count += bag[1]
        buffer.extend(bag[1] * rules[bag[0]])
    print(f'Part 2: {count}')