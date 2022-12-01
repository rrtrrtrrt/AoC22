# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:25:41 2022

@author: User
"""

# Part one

calories = 0
elf_nr = 1
solution = [0, 0]

with open('input.txt') as f:
    for line in f:
        if line == "\n":
            if calories > solution[1]:
                solution = [elf_nr, calories]
            elf_nr = elf_nr + 1
            calories = 0
        else:
            calories = calories + int(line.strip('\n'))

print("Elf number " + str(solution[0]) + " is carrying " + str(solution[1]) + " calories.")   


# Part two
    
Elf_List = []
calories = 0
elf_nr = 1

with open('input.txt') as f:
    for line in f:
        if line == "\n":
            Elf_List.append(calories)
            elf_nr = elf_nr + 1
            calories = 0
        else:
            calories = calories + int(line.strip('\n'))

Elf_List.sort(reverse=True)
print("The top three elves are carrying " + str(Elf_List[0] + Elf_List[1] + Elf_List[2]) + " calories.")