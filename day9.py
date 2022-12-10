#%%
import numpy as np
import matplotlib.pyplot as plt

with open('data\day9_input.txt') as f:
    lines = f.readlines()
lines = [line.strip('\n') for line in lines]

string_path = ['0,0']
string_path *= 10

x_cor = 0
y_cor = 0
last_x_cor = 0
last_y_cor = 0


# fig, ax = plt.subplots(figsize=(5, 5))
for line in lines:
    for _ in range(int(line.split()[1])):
        if line.split()[0] == 'L':
            x_cor -= 1
        if line.split()[0] == 'R':
            x_cor += 1
        if line.split()[0] == 'U':
            y_cor += 1
        if line.split()[0] == 'D':
            y_cor -= 1   
    
        dist = ((head_x_cor-tail_x_cor)**2 + (head_y_cor-tail_y_cor)**2)**0.5
        if dist >= 2:
            tail_x_cor = last_head_x_cor
            tail_y_cor = last_head_y_cor

        last_head_x_cor = head_x_cor
        last_head_y_cor = head_y_cor
        head_path.append(str(head_x_cor) + ',' + str(head_y_cor))
        tail_path.append(str(tail_x_cor) + ',' + str(tail_y_cor))
        # print(str(head_x_cor)+','+str(head_y_cor)+'    '+str(tail_x_cor)+','+str(tail_y_cor))
        # plt.xlim([-80, 30])
        # plt.ylim([-80, 30])        
        # plt.plot(head_x_cor,head_y_cor, 'o')
        # plt.plot(tail_x_cor,tail_y_cor, 'x')
        # plt.pause(0.001)
        # plt.clf()
        
#%%
# plt.show()
part1_ans = len(set(tail_path))
print(part1_ans)
