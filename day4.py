#%%
import numpy as np
import re

with open('data\day4_input.txt') as f:
    pairs = f.readlines()


all_overlaps = []
any_overlaps = []
for pair in pairs:
    numbers = re.findall(r'\d+', pair)  
    numbers = [int(number) for number in numbers]
    first_start = numbers[0]
    first_end = numbers[1]
    second_start = numbers[2]
    second_end = numbers[3]
    if (first_start<=second_start and first_end>=second_end) or (second_start<=first_start and second_end>=first_end):
        all_overlaps.append(numbers)
    if not(first_end<second_start or second_end<first_start):
        any_overlaps.append(numbers)
        
print(len(all_overlaps))
print(len(any_overlaps))