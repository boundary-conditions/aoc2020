#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:25:33 2020

@author: charleskeenan
"""
import aocmodule as aoc

puzzle_input = aoc.input_getter('day_8_input.txt')

p = [[x.split()[0], int(x.split()[1])] for x in puzzle_input]
    
def handheld(p, index=0, instruction=None):
    if instruction != None:
        if instruction[0] == 'nop':
            instruction[0] = 'jmp'
            p[index] = instruction
        elif instruction[0] == 'jmp':
            instruction[0] = 'nop'
            p[index] = instruction
    
    current_index = 0
    next_index = None
    accumulator = 0
    list_of_indexes = []
    while True:
        infinite = False
        try:
            if p[current_index][0] == 'acc':
                accumulator += p[current_index][1]
                next_index = current_index + 1
                if next_index in list_of_indexes:
                    #print(f"The accumulator is {accumulator} before instruction {next_index} is executed a second time")
                    infinite = True
                    break
                else:
                    list_of_indexes.append(current_index)
                    current_index = next_index
            elif p[current_index][0] == 'jmp':
                next_index = current_index + p[current_index][1]
                if next_index in list_of_indexes:
                    #print(f"The accumulator is {accumulator} before instruction {next_index} is executed a second time")
                    infinite = True
                    break
                else:
                    list_of_indexes.append(current_index)
                    current_index = next_index
            elif p[current_index][0] == 'nop':
                next_index = current_index + 1
                if next_index in list_of_indexes:
                    #print(f"The accumulator is {accumulator} before instruction {next_index} is executed a second time")
                    infinite = True
                    break
                else:
                    list_of_indexes.append(current_index)
                    current_index = next_index
        except:
            print(f"Accumulator is {accumulator} when program ends")
            break
                    
                    
                    
    return infinite
                
for i in range(len(p)):
    index = i
    if p[index][0] == 'nop' or p[index][0] == 'jmp':
         infinite = handheld(p, index, p[index])
         if infinite:
             p = [[x.split()[0], int(x.split()[1])] for x in puzzle_input]
             continue
         else:
             break
    