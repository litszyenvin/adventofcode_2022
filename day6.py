#%%
import numpy as np

with open('data\day6_input.txt') as f:
    raw = f.readlines()
signal = raw[0]
BUNCH_LENGTH = 14
for i, letter in enumerate(signal):
    bunch = signal[i:i+BUNCH_LENGTH]
    if len(set(bunch)) == len(bunch):
        print(bunch)
        print (i+BUNCH_LENGTH)
        break


