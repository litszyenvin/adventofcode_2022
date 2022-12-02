import numpy as np

# data = np.loadtxt('data\day1_input.txt')
# print (data)
with open('data\day2_input.txt') as f:
    rounds = f.readlines()
    # print (lines)

score_from_result = []
score_from_move = []

for round in rounds:
    # print(round)
    opponent = round[0]
    me = round[2]
    new_result = round[2]
    
    if opponent == 'A':
        if new_result == 'X': #lose:
            me = 'Z'
        elif new_result == 'Y': #draw
            me = 'X'
        else:
            me = 'Y'

    if opponent == 'B':
        if new_result == 'X': #lose:
            me = 'X'
        elif new_result == 'Y': #draw
            me = 'Y'
        else:
            me = 'Z'

    if opponent == 'C':
        if new_result == 'X': #lose:
            me = 'Y'
        elif new_result == 'Y': #draw
            me = 'Z'
        else:
            me = 'X'

    if (me == 'X' and opponent == 'C') or (me == 'Y' and opponent == 'A') or (me == 'Z' and opponent == 'B'):
        this_round_result = 6
    elif (me == 'X' and opponent == 'A') or (me == 'Y' and opponent == 'B') or (me == 'Z' and opponent == 'C'):
        this_round_result = 3
    else:
        this_round_result = 0
    
    if me == 'X':
        this_round_move = 1
        # new_result = 1
    if me == 'Y':
        this_round_move = 2
        # new_result = 4
    if me == 'Z':
        this_round_move = 3
        # new_result = 7

    score_from_result.append(this_round_result)
    score_from_move.append(this_round_move)
    # print('raw = ' + round + 'score_from_new_result = ' + str(new_result))

total_score = sum(score_from_result) + sum(score_from_move)
print(total_score)