# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:04:06 2022

@author: User
"""
# Part one

sum_of_priorities = 0

with open('input.txt') as f:
    for line in f:
        n = len(line)
        first_compartment = set(line[0:n//2])
        second_compartment = set(line[n//2:n])
        for char in first_compartment:
            if char in second_compartment:
                if ord(char) > 95:
                    sum_of_priorities = sum_of_priorities + ord(char) - 96
                else:
                    sum_of_priorities = sum_of_priorities + ord(char) - 38
print("The sum of priorities is " + str(sum_of_priorities))


# Part two

sum_of_priorities_part_two = 0
elf_counter = 1

with open('input.txt') as f:
    for line in f:
        if elf_counter == 1:
            first_elf = set(line)
            elf_counter = 2
        elif elf_counter == 2:
            second_elf = set(line)
            elf_counter = 3
        elif elf_counter == 3:
            third_elf = set(line)
            for char in first_elf:
                if char in second_elf and char in third_elf:
                    if char != "\n" and ord(char) > 95:
                        sum_of_priorities_part_two = sum_of_priorities_part_two + ord(char) - 96
                    elif char != "\n" and ord(char) <= 95:
                        sum_of_priorities_part_two = sum_of_priorities_part_two + ord(char) - 38  
            elf_counter = 1
print("The sum of priorities for part two is " + str(sum_of_priorities_part_two))