#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:18:39 2020

@author: charleskeenan
"""

import re
KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
file = open('day_4_input.txt', 'r')

# separate into a list of passport chunks
allPassports = file.read().split('\n\n')

# convert the chunks into key/value pairs
def cleanPassport(p):
    pairs = [(k, v) for (k, v) in [row.split(':') for row in [row for row in re.split('[\n|\s]', p)]]]
    return pairs

def check1(passport):
    """
    Returns false if one of the keys is not present in this passport,
    otherwise it returns true and is added to a list of valid passports.
    """
    keysInThisPassPort = [pair[0] for pair in passport]
    for key in KEYS:
        if key not in keysInThisPassPort:
            return False
    
    return True

def check2(passport):
    """
    Matches the key to the key in a dict to run lambdas that return true/false.
    If any of them evaluates false the function returns false and the passport
    isn't added to the list of valid passports.
    """
    keyChecks = {
        'byr': lambda v : int(v) >= 1920 and int(v) <= 2002,
        'iyr': lambda v : int(v) >= 2010 and int(v) <= 2020,
        'eyr': lambda v : int(v) >= 2020 and int(v) <= 2030,
        'hgt': lambda v : bool(re.match("^(1[5-8][0-9]|19[0-3])(cm)$|^(59|6[0-9]|7[0-6])(in)$", v)),
        'hcl': lambda v : bool(re.match('^#([0-9]|[a-f]){6}$', v)),
        'ecl': lambda v : v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda v : bool(re.match("^[0-9]{9}$", v)),
        'cid': lambda v : True if v else True
        }

    # what passport looks like now:
    # [('xxx', 'xxxxx'), ('xxx', 'xxxxxxx'), ('xxx', 'xxxxxxx')]
    for pair in passport:
        # what pair looks like now:
        # ('xxx', 'xxxxxx')
        k = pair[0]
        v = pair[1]
        if not keyChecks[k](v):
            return False
    
    return True
    
# split up the input file into a cleaner list
cleanedPassports = [cleanPassport(p) for p in allPassports]

# check for Part 1: valid passports based on keys present
validPassports1 = [p for p in cleanedPassports if check1(p)]

# check for Part 2: valid passports based on valid keys
validPassports2 = [p for p in validPassports1 if check2(p)]

print(len(list(validPassports2)))