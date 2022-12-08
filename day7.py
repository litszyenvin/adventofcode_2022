#%%
import numpy as np
from functools import reduce  # forward compatibility for Python 3
import operator
import pandas as pd
import json

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    if isinstance(value, dict):
        dic[keys[-1]].update(value)
    else:
        dic[keys[-1]] = value

def myprint(d):
    for key, content in d.items():
        # print('current_path:' + str(key))
        if isinstance(content, dict):
            # print(key)
            myprint(content)
        else:
            # print("{0} ; {1}".format(key, content))
            for set in unique_dirs:
                if set in key:
                    folder_sizes[set] += content
                    folder_levels[set].append(key.index(set))



with open('data\day7_input.txt') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]
#%%
mydrive = {'/':{}}
reading_mode = False
current_dir = ['/']
file_index = 0
all_dirs = []
new_all_dirs = []
# df = pd.DataFrame()
first_line = True
for count, line in enumerate(lines):    
    if line.split()[1] == 'cd':
        file_index = 0
        # if count != 0:
            # temp_df = pd.DataFrame({current_dir[-1]+'_sizes':file_sizes})
            # file_sizes = []
            # df = pd.concat([df, temp_df], axis=1)
            # temp_df = pd.DataFrame({current_dir[-1]+'_dirs':dir_names})
            # dir_names = []
            # df = pd.concat([df, temp_df], axis=1)
            # df[current_dir[-1]+'_sizes'] = file_sizes
            # df[current_dir[-1]+'_dirs'] = dir_names

        if line == '$ cd /':
            current_dir = ['/']
        elif line == '$ cd ..':
            current_dir = current_dir[:-1]
        else:
            current_dir += [line.split()[2]]
    elif line.split()[1] == 'ls':
        reading_mode = True
    elif line.split()[0] == 'dir': #when contain dir
        nested_set(mydrive, current_dir, {line.split()[1]:{}})
        folder_level = len(current_dir)
        all_dirs.append(line.split()[1])
        new_all_dirs.append([[line.split()[1]], folder_level])

        # dir_names.append(line.split()[1])
    elif line.split()[0][0].isdigit(): #when contain file
        nested_set(mydrive, current_dir + [str(current_dir) + str(file_index)], int(line.split()[0]))
        # file_sizes.append(str(line.split()[0]))
        file_index += 1
#%%
# print(all_dirs)

global unique_dirs
unique_dirs = set(all_dirs)
unique_dirs.add('/')
global folder_sizes
folder_sizes = dict.fromkeys(unique_dirs, 0)
global folder_levels
folder_levels = dict.fromkeys(unique_dirs, [])

myprint(mydrive)
# print (folder_sizes)
part1_ans = 0
for key, content in folder_sizes.items():
    if content < 100000:
        part1_ans += content
#%%
print(part1_ans)
# print(folder_levels)
# json_object = json.dumps(mydrive, indent = 4) 
# print(json_object)


