#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:21:24 2020

@author: charleskeenan
"""   

### Part 1
def part1(run, puzzle):
    if not run:
        return
    required_fields = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False
    }
    valid_passports = 0
    for item in puzzle:
        # Break up line into individual fields, then extract field name
        fields = [i.split(":")[0] for i in item.split()]
        for f in fields:
            if f != "cid":
                required_fields[f] = True
        if item == "" or puzzle.index(item) == len(puzzle)-1:
            # New passport. Track validity, reset and continue
            if all(list(required_fields.values())):
                # All required fields were found.
                valid_passports += 1
            # Reset
            for key in required_fields.keys():
                required_fields[key] = False
            continue

    return valid_passports

### Part 2
def validate_byr(byr: str):
    return len(byr) == 4 and 2002 >= int(byr) >= 1920
def validate_iyr(iyr):
    return len(iyr) == 4 and 2020 >= int(iyr) >= 2010
def validate_eyr(eyr):
    return len(eyr) == 4 and 2030 >= int(eyr) >= 2020
def validate_hgt(hgt):
    return (hgt[-2:] == "cm" and 193 >= int(hgt[:-2]) >= 150) or \
           (hgt[-2:] == "in" and 76 >= int(hgt[:-2]) >= 59)
def validate_hcl(hcl):
    return hcl[0] == "#" and len(hcl) == 7 and \
        all([i in "abcdef1234567890#" for i in hcl])
def validate_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def validate_pid(pid):
    return len(pid) == 9

validate = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
}

def part2(run, puzzle):
    if not run:
        return
    required_fields = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False
    }
    valid_passports = 0
    for item in puzzle:
        # Break up line into individual fields, then extract field name
        fields = [i.split(":") for i in item.split()]
        for f in fields:
            if f[0] != "cid":
                required_fields[f[0]] = validate[f[0]](f[1])
        if item == "" or puzzle.index(item) == len(puzzle)-1:
            # New passport. Track validity, reset and continue
            if all(list(required_fields.values())):
                # All required fields were found.
                valid_passports += 1
            # Reset
            for key in required_fields.keys():
                required_fields[key] = False

    return valid_passports

with open('day_4_input.txt') as puzzle:
    p = [line.strip() for line in puzzle]
    print(part1(True, p))   # Result: 219
    print(part2(True, p))   # Result: 127 