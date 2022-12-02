import numpy as np

# data = np.loadtxt('data\day1_input.txt')
# print (data)
with open('data\day1_input.txt') as f:
    lines = f.readlines()
    # print (lines)

list_of_sums = []
sum = 0
for line in lines:
    line = line.strip('\n')
    if line != '':
        number = int(line)
        sum = sum + number
    else:
        # print(sum)
        list_of_sums.append(sum)
        sum = 0

print(max(list_of_sums))
