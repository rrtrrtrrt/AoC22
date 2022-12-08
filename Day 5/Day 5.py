# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:58:02 2022

@author: User
"""
# Part one

with open('input.txt') as f:
    data = f.read()
    
stacks = data.strip().split("\n\n")[0]
instructions = data.strip().split("\n\n")[1]
instructions = instructions.split("\n")

for line in stacks.split("\n"):
    if "fields" not in locals():
        fields = {key: [] for key in range(1, (len(line)+1)//4+1)}
    for n, m in zip(range(0, len(line), 4), range(1, (len(line)+1)//4+1)):
        fields[m].append(line[n:n+4])
        
for i in fields:
    fields[i].reverse()
    while("    " in fields[i]):
        fields[i].remove("    ")
    while("   " in fields[i]):
        fields[i].remove("   ")

# For the solution to Part one uncomment the following block and comment out Part two   
# for line in instructions:
#     for i in range(1, int(line.split(" ")[1])+1):
#         fields[int(line.split(" ")[5])].append(fields[int(line.split(" ")[3])].pop())

# for i in fields:
#     print(fields[i][-1])
    

# Part two
bus = []
for line in instructions:
    for i in range(1, int(line.split(" ")[1])+1):
        bus.append(fields[int(line.split(" ")[3])].pop())
    for i in range(0, len(bus)):
        fields[int(line.split(" ")[5])].append(bus.pop())

for i in fields:
    print(fields[i][-1])

