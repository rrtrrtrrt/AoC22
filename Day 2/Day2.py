# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:53:40 2022

@author: User
"""
# Part one

round_score = 0
total_score = 0

with open('input.txt') as f:
    for line in f:
        line = line.replace("X", "1")
        line = line.replace("Y", "2")
        line = line.replace("Z", "3")
        line = line.replace("A", "1")
        line = line.replace("B", "2")
        line = line.replace("C", "3")
        round_score = int(line[2])
        if line[0] == line[2]:
            round_score = round_score + 3
        elif int(line[0]) == int(line[2])-1 or line[0] == "3" and line[2] == "1":
            round_score = round_score + 6
        total_score = total_score + round_score
         
print("Total score is " + str(total_score))


# Part two

round_score = 0
total_score = 0
match_list = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

with open('input.txt') as f:
    for line in f:
        line = line.replace("X", "1")
        line = line.replace("Y", "2")
        line = line.replace("Z", "3")
        line = line.replace("A", "1")
        line = line.replace("B", "2")
        line = line.replace("C", "3")
        if line[2] == "1":
            round_score = match_list[int(line[0])-1][2]
        elif line[2] == "2":
            round_score = match_list[int(line[0])-1][0] + 3       
        elif line[2] == "3":
            round_score = match_list[int(line[0])-1][1] + 6   
        total_score = total_score + round_score

print("Total score for part two is " + str(total_score))