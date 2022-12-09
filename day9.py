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

def findViewScore(value, arr):    
    if (value>arr).sum()==arr.size:
        score = len(arr)
    else:
        score = np.min(np.where((arr>=value)==True)) + 1
    return score
    
    

for row_idx in range(map.shape[0]):
    for col_idx in range(map.shape[1]):
        current_height = map[row_idx,col_idx]
        # print(current_height)
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
# print(visible_count)
# %%
row_score = []
map_score = []
view_to_right = view_to_left = view_to_down = view_to_up = 0
for row_idx in range(map.shape[0]):
    for col_idx in range(map.shape[1]):
        current_height = map[row_idx,col_idx]
        # print(current_height)
        slice_to_right = map[row_idx,col_idx+1:]
        slice_to_left = map[row_idx,:col_idx]
        slice_to_down = map[row_idx+1:,col_idx]
        slice_to_up = map[:row_idx,col_idx]
        
        if col_idx != map.shape[1] or row_idx != map.shape[0]:

            if len(slice_to_right)!=0:        
                view_to_right = findViewScore(current_height, slice_to_right)
            # print(view_to_right)
            if len(slice_to_left)!=0:
                view_to_left = findViewScore(current_height, np.flip(slice_to_left))
            # print(view_to_left)
            if len(slice_to_down)!=0:
                view_to_down = findViewScore(current_height, slice_to_down)
            # print(view_to_down)
            if len(slice_to_up)!=0:
                view_to_up = findViewScore(current_height, np.flip(slice_to_up))
            # print(view_to_up)
          
        scenic_score = view_to_right * view_to_left * view_to_down * view_to_up
        row_score.append(scenic_score)
        # print(row_score)
        view_to_right = view_to_left = view_to_down = view_to_up = 0

    map_score.append(row_score)
    # print(map_visible)
    row_score = []

# print(map_score)
print(np.max(np.array(map_score)))