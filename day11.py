import numpy as np
from math import floor

# with open('data\day10_input.txt') as f:
#     lines = f.readlines()
# lines = [line.strip('\n') for line in lines]
monkeys = [[]]*8
monkeys[0] = [56, 56, 92, 65, 71, 61, 79]
monkeys[1] = [61, 85]
monkeys[2] = [54, 96, 82, 78, 69]
monkeys[3] = [57, 59, 65, 95]
monkeys[4] = [62, 67, 80]
monkeys[5] = [91]
monkeys[6] = [79, 83, 64, 52, 77, 56, 63, 92]
monkeys[7] = [50, 97, 76, 96, 80, 56]

for monkey in monkeys:
    for item in monkey:
        item = float(item)

inspects = [0]*8

def monkey_throw(monkeys, id, operation, operation_num, test_num, ifTrueTo, ifFlaseTo):
    if operation == '+':  
        monkeys[id] = [item+operation_num for item in monkeys[id]]
    elif operation == '-':  
        monkeys[id] = [item-operation_num for item in monkeys[id]]
    elif operation == '*':  
        monkeys[id] = [item*operation_num for item in monkeys[id]]
    elif operation == '/':  
        monkeys[id] = [item/operation_num for item in monkeys[id]]
    else:  
        monkeys[id] = [item**operation_num for item in monkeys[id]]
    
    monkeys[id] = [floor(item/3) for item in monkeys[id]]
    inspects[id] += len(monkeys[id])
    for item in monkeys[id]:
        if item%test_num == 0:
            monkeys[ifTrueTo].append(item)
        else:
            monkeys[ifFlaseTo].append(item)
    monkeys[id] = []

def monkey_throw_part2(monkeys, id, operation, operation_num, test_num, ifTrueTo, ifFlaseTo):
    if operation == '+':  
        monkeys[id] = [item+operation_num for item in monkeys[id]]
    elif operation == '-':  
        monkeys[id] = [item-operation_num for item in monkeys[id]]
    elif operation == '*':
        monkeys[id] = [item*operation_num for item in monkeys[id]]
    elif operation == '/':  
        monkeys[id] = [item/operation_num for item in monkeys[id]]
    else:  
        monkeys[id] = [item**operation_num for item in monkeys[id]]
    
    inspects[id] += len(monkeys[id])
    for item in monkeys[id]:
        if item%test_num == 0:
            if operation == '**':
                new_item = 1
            else:
                new_item = item
            monkeys[ifTrueTo].append(new_item)
        else:
            if operation == '**':
                new_item = (item%13)**2
            else:
                new_item = item
            monkeys[ifFlaseTo].append(new_item)
    monkeys[id] = []



for round in range(20):
    monkey_throw(monkeys, 0, '*', 7, 3, 3, 7)
    monkey_throw(monkeys, 1, '+', 5, 11, 6, 4)
    monkey_throw(monkeys, 2, '**', 2, 7, 0, 7)
    monkey_throw(monkeys, 3, '+', 4, 2, 5, 1)
    monkey_throw(monkeys, 4, '*', 17, 19, 2, 6)
    monkey_throw(monkeys, 5, '+', 7, 5, 1, 4)
    monkey_throw(monkeys, 6, '+', 6, 17, 2, 0)
    monkey_throw(monkeys, 7, '+', 3, 13, 3, 5)
    # print(str(round/10000*100) + '%')

inspects = sorted(inspects)
print(inspects)
# print(inspects)
part1_ans = inspects[-1]*inspects[-2]
print(part1_ans)



