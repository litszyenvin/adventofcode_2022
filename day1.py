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

list_of_sums = sorted(list_of_sums)
print(list_of_sums)

sum_of_top3 = list_of_sums[-1] + list_of_sums[-2] + list_of_sums[-3]
print(sum_of_top3)
