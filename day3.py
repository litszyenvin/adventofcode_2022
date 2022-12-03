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
    for letter in first_half:
        if letter in second_half:
            duplicate = letter
            duplicates.append(duplicate)

print(duplicates)
for letter in duplicates:
    if letter.islower():
        priority = ord(letter) - 96
    else:
        priority = ord(letter) - 38
    priorties.append(priority)

print(priorties)
