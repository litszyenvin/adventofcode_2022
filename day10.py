#%%
import numpy as np
from math import floor

with open('data\day10_input.txt') as f:
    lines = f.readlines()
lines = [line.strip('\n') for line in lines]
X = [1]
temp_X = 1
#%%
for line in lines:
    if len(line.split()) == 2:
        X.append(temp_X)
        temp_X += int(line.split()[1])
        X.append(temp_X)
    else:
        X.append(temp_X)

#%%    
part1_ans = (20*X[19] + 60*X[59] + 100*X[99] + 140*X[139] + 180*X[179] + 220*X[219])
print(part1_ans)


lit = [0]*241
for cycle, _ in enumerate(X):
    adjusted_X = floor(cycle/40)*40 + X[cycle]
    if adjusted_X == cycle or adjusted_X+1 == cycle or adjusted_X-1 == cycle:
        lit[cycle] = 1
    else:
        lit[cycle] = 0

for pixel, _ in enumerate(lit):
    if lit[pixel] == 1:
        print('#', end='')
    else:
        print('.', end = '')
    if (pixel+1)%40 == 0:
        print('')
