# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:32:55 2022

@author: User
"""
# Part one

counter = 0

with open('input.txt') as f:
    for line in f:
        pairs = line.split(",")
        sectors1 = pairs[0].split("-")
        sectors2 = pairs[1].split("-")
        if int(sectors1[0]) <= int(sectors2[0]) and int(sectors1[1]) >= int(sectors2[1]): 
            counter += 1
        elif int(sectors2[0]) <= int(sectors1[0]) and int(sectors2[1]) >= int(sectors1[1]): 
            counter += 1
print("The number of pairs that meet the criteria is " + str(counter))


# Part two

counter2 = 0

with open('input.txt') as f:
    for line in f:
        pairs = line.split(",")
        sectors1 = pairs[0].split("-")
        sectors2 = pairs[1].split("-")
        if int(sectors1[0]) in range(int(sectors2[0]), int(sectors2[1])+1): 
            counter2 += 1
        elif int(sectors1[1]) in range(int(sectors2[0]), int(sectors2[1])+1): 
            counter2 += 1
        elif int(sectors2[0]) in range(int(sectors1[0]), int(sectors1[1])+1): 
            counter2 += 1
        elif int(sectors2[1]) in range(int(sectors1[0]), int(sectors1[1])+1): 
            counter2 += 1
print("The number of pairs that overlap at all is " + str(counter2))