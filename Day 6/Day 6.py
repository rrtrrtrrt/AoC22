# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:47:04 2022

@author: User
"""
# Part one

last_four_chars = []
char_counter = 4

with open('input.txt') as f:
    data = f.read()

for char in data:
    if len(last_four_chars) < 4:
        last_four_chars.append(char)
    elif len(last_four_chars) == 4:
        last_four_chars.pop(0)
        last_four_chars.append(char)
        char_counter += 1
        if len(set(last_four_chars)) == 4:
            print("First start-of-packet marker is after character " + str(char_counter))
            break
    
# Part two

last_fourteen_chars = []
char_counter = 14

for char in data:
    if len(last_fourteen_chars) < 14:
        last_fourteen_chars.append(char)
    elif len(last_fourteen_chars) == 14:
        last_fourteen_chars.pop(0)
        last_fourteen_chars.append(char)
        char_counter += 1
        if len(set(last_fourteen_chars)) == 14:
            print("First start-of-message marker is after character " + str(char_counter))
            break