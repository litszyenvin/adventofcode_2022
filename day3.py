#%%
import numpy as np

with open('data\day3_input.txt') as f:
    rucksacks = f.readlines()

duplicates = []
priorties = []


for rucksack in rucksacks:
    half_length = int(len(rucksack)/2)
    first_half = rucksack[0:half_length]
    second_half = rucksack[half_length:]
    # print(first_half)
    # print(second_half)
    for letter in first_half:
        if letter in second_half:
            duplicate = letter
    duplicates.append(duplicate)
    # print(duplicate)
#%%
# print(duplicates)
for letter in duplicates:
    if letter.islower():
        priority = ord(letter) - 96
    else:
        priority = ord(letter) - 38
    priorties.append(priority)

print(sum(priorties))
# %%
groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]
# print(groups)

#%%
bedges = []
bedges_priorities = []
for group in groups:
    for letter in (group[0].strip('\n')):
        if (letter in group[1]) and (letter in group[2]):
            bedge = letter
    print(group[0])
    print(group[1])
    print(group[2])
    print(bedge)
    bedges.append(bedge)
        

for letter in bedges:
    if letter.islower():
        priority = ord(letter) - 96
    else:
        priority = ord(letter) - 38
    bedges_priorities.append(priority)

print(len(bedges_priorities))
print(sum(bedges_priorities))
# %%
