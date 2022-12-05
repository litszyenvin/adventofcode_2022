#%%
import numpy as np
from math import floor
import re

np.set_printoptions(threshold=10000000000)
NO_OF_COLUMNS = 9
INITIAL_HEIGHT = 7

with open('data/day5_input.txt') as f:
    rows = f.readlines()
stack = np.empty((9,100), dtype=str)
stack_list = []
# column_index = 0
row_index = INITIAL_HEIGHT
for x, row in enumerate(rows):
    if x <= 8:
        column_indexes = [m.start() for m in re.finditer('[A-Z]', row)]
        letters = re.findall('[A-Z]', row)
        for i, index in enumerate(column_indexes):
            column_indexes[i] = floor(column_indexes[i]/4)
            stack[column_indexes[i]][row_index] = letters[i]
        
        row_index -= 1

for i in range(0,NO_OF_COLUMNS):
    stack_list.append(stack[i][stack[i]!=''].tolist())
# print(stack_list)

#%%
for x, row in enumerate(rows):
    if x > 9:
        instruction = re.findall('\d+',row)
        # print(instruction)
        height = int(instruction[0])
        origin = int(instruction[1])
        destination = int(instruction[2])
        temp = stack_list[origin-1][-height:]
        # temp = temp[::-1]
        stack_list[origin-1] = stack_list[origin-1][:len(stack_list[origin-1])-height]
        stack_list[destination-1] = stack_list[destination-1] + temp

for column in stack_list:
    print(column[-1], end='')


