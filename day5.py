import pandas as pd
import numpy as np

def process_stack_row(row):
    row = row[1::4]
    
    stack = [None] * (len(row))
    for item in range(0,len(row)):
        if row[item] != ' ':
            stack[item] = row[item]
    return stack

def get_top(stack):
    return stack[0]

def run_part_one(stacks,moves):
    ind = 0
    crane_move = pd.DataFrame(0, index=np.arange(len(moves)), columns=['move','from','to'])
    for row in moves:
        elements = row.split()
        crane_move.loc[ind] = elements[1::2]
        ind += 1 

    for index,move,src,to in crane_move.itertuples():
        for i in range(0,int(move)):
            crane_hold = stacks[int(src)-1].pop(0)
            stacks[int(to)-1].insert(0,crane_hold) 
            
        
    part1 = ''
    for stack in stacks:
        part1= part1 + stack[0]

    print('Part 1: ',part1)

def run_part_two(stacks2,moves):
    ind = 0
    crane_move = pd.DataFrame(0, index=np.arange(len(moves)), columns=['move','from','to'])
    for row in moves:
        elements = row.split()
        crane_move.loc[ind] = elements[1::2]
        ind += 1 

    for index,move,src,to in crane_move.itertuples():
        crane_hold = stacks2[int(src)-1][0:int(move)]
        del stacks2[int(src)-1][0:int(move)]
        for j in range(len(crane_hold),0,-1):
            stacks2[int(to)-1].insert(0,crane_hold[j-1]) 
            
    part2 = ''
    for stack in stacks2:
        part2 = part2 + stack[0]

    print('Part 2: ',part2)

filename = "./inputs/day5_input.txt"

with open(filename,'r') as f:
    rows = f.read().split('\n')

stacks = []
ind = 0
row = rows[ind]
while 'move' not in row:
    stacks.append(process_stack_row(row))
    ind += 1
    row = rows[ind]
df = pd.DataFrame(stacks[:-2])
df = df.transpose()
stacks = df.values.tolist()
stacks2 =  df.values.tolist()
moves = rows[ind:]

for i in range(0,len(stacks)):
    stacks[i] =[j for j in stacks[i] if j is not None]
    stacks2[i] =[j for j in stacks2[i] if j is not None]


run_part_one(stacks,moves)

run_part_two(stacks2,moves)

