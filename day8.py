#%%
import numpy as np

with open('data\day8_input.txt') as f:
    lines = f.readlines()
lines = [line.strip('\n') for line in lines]
row = []
map_list = []
for line in lines:    
    for num in line:
        row.append(int(num))
    map_list.append(row)
    row = []
map = np.array(map_list)
# print(map)

visible_count = 0
map_visible = []
row_visible = []
vis_from_right = False
vis_from_left = False
vis_from_down = False
vis_from_up = False

for row_idx in range(map.shape[0]):
    for col_idx in range(map.shape[1]):
        current_height = map[row_idx,col_idx]
        print(current_height)
        if (current_height>map[row_idx,col_idx+1:]).sum()==map[row_idx,col_idx+1:].size:
            vis_from_right = True
        if (current_height>map[row_idx,:col_idx]).sum()==map[row_idx,:col_idx].size:
            vis_from_left = True
        if (current_height>map[row_idx+1:,col_idx]).sum()==map[row_idx+1:,col_idx].size:
            vis_from_down = True
        if (current_height>map[:row_idx,col_idx]).sum()==map[:row_idx,col_idx].size:
            vis_from_up = True

        if vis_from_right == True or vis_from_left == True or vis_from_down == True or vis_from_up == True:
            visible = 1
            visible_count += 1
        row_visible.append(visible)
        visible = 0
        vis_from_right = vis_from_left = vis_from_down = vis_from_up = False

    map_visible.append(row_visible)
    # print(map_visible)
    row_visible = []
#%%
# print(map_visible)
print(np.sum(np.array(map_visible)))
print(visible_count)
# %%
