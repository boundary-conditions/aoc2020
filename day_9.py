#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 07:03:05 2020

@author: charleskeenan
"""

import aocmodule as aoc

input_list = aoc.input_getter('day_9_input.txt')
p = [int(x) for x in input_list]


#p = [35, 20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309, 576]

location = 25
#part_two_number = 22406676

class XMas:
    def __init__(self, puzzle_input, preamble_length):
        self.backup_p = [x for x in puzzle_input]
        self.p = puzzle_input
        self.l = preamble_length

    
    def summer(self):
        to_sum = self.p[:self.l]
        self.sums_list = []
        for a in range(self.l):
            sums = [to_sum[a] + x for x in to_sum if to_sum[a] != x]
            for i in sums:
                if i not in self.sums_list:
                    self.sums_list.append(i)
        return self.sums_list
    
    def checker(self):
        if self.p[self.l] in self.sums_list:
            return True
        
    def mover(self):
        self.p = self.p[1:]
        return None
        
    def finder(self, number_to_find):
        count, i = 0, 0
        while True:
            if count == number_to_find:
                 self.backup_p = self.backup_p[:i]
                 output = True
                 break
            elif count > number_to_find:
                 self.backup_p = self.backup_p[1:]
                 output = False
                 break
            else:
                 count += self.backup_p[i]
                 i += 1
        return output
        
        
xmas = XMas(p, 25)
while True:
    xmas.summer()
    if xmas.checker():
        xmas.mover()
    else:
        print(xmas.p[xmas.l])
        part_two_number = xmas.p[xmas.l]
        break
while True:
    if xmas.finder(part_two_number):
        print(xmas.backup_p)
        break
xmas.backup_p.sort()
part_two_answer = xmas.backup_p[0] + xmas.backup_p[-1]
    


