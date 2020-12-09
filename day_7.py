#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:29:01 2020

@author: charleskeenan
"""

puzzle_input = open('day_7_input.txt').read().split('\n')


puzzle_input = puzzle_input[:-1]
#bag_dictionary = {}
second_bag = {}
# for item in puzzle_input:
#     bag_list = []
#     bag = []
#     bag_and_contents = item.split(' bags contain ')
#     for content in bag_and_contents[1].split():
#         if content.isdigit():
#             continue
#         elif 'bag' in content:
#             bag = ' '.join(bag)
#             bag_list.append(bag)
#             bag = []
#         else:
#             bag.append(content)
#     bag_dictionary[bag_and_contents[0]] = bag_list


# final_list = [key for key, value in bag_dictionary.items() if 'shiny gold' in value]
# working_list = []
# first_result = len(final_list)
# def first_thing(working_list, final_list):
#     for colour in final_list:
#         working_list.append([key for key, value in bag_dictionary.items() if colour in value])
#     for item in working_list:
#         for colour in item:
#             if colour not in final_list:
#                 final_list.append(colour)
#     return working_list, final_list

# while True:
#     working_list, final_list = first_thing(working_list, final_list)
#     if first_result == len(final_list):
#         break
#     else:
#         first_result = len(final_list)

# print(first_result)


for item in puzzle_input:
    bag_list = []
    bag = []
    bag_and_contents = item.split(' bags contain ')
    for content in bag_and_contents[1].split():
        if content.isdigit():
            num_of_colour = int(content)
            bag_list.append(num_of_colour)
        elif 'other' in content:
            bag = '#'
            bag_list.append(bag)
            bag = []
            continue
        elif 'bag' in content:
            bag = ' '.join(bag)
            bag_list.append(bag)
            bag = []
        else:
            bag.append(content)
    second_bag[bag_and_contents[0]] = bag_list

num_of_bags = 0
second_result = 0
bag_colour = 'shiny gold'
current_bag = second_bag[bag_colour]
# while True:
#     pass
#     num_of_bags = sum([x for x in current_bag if type(x) == int])
#     second_result += num_of_bags
#     for i in range(1, len(current_bag), 2):
#         num_of_bags = sum([x for x in second_bag['shiny gold'] if type(x) == int])
        
    








































