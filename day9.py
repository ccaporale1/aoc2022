import numpy as np
verbose = True
# function to update map
def move_head(direction,rope_map,tracking_map,tail_locations):
    head_loc = list(zip(*np.where(rope_map == 'H')))[0]
    if verbose: print('updating head at location: ',head_loc)
    if direction == 'R':
        next_head_loc = list(head_loc)
        next_head_loc[1] = next_head_loc[1] + 1
        next_head_loc = tuple(next_head_loc)
        if verbose: print('trying to move to column ',next_head_loc[1],' and map has ',len(rope_map)-1,' columns')
        if next_head_loc[1] > len(rope_map[0])-1:
            rope_map = np.hstack((rope_map,np.full((len(rope_map)),'.')[:, np.newaxis]))
            tracking_map = np.hstack((tracking_map,np.zeros((len(tracking_map)))[:, np.newaxis]))
    elif direction == 'L':
        next_head_loc = list(head_loc)
        next_head_loc[1] = next_head_loc[1] -1
        if next_head_loc[1] < 0:
            rope_map = np.hstack((np.full((len(rope_map)),'.')[:, np.newaxis],rope_map))
            tracking_map = np.hstack((np.zeros((len(tracking_map)))[:, np.newaxis],tracking_map))
            next_head_loc[1] = 0
            head_loc = list(head_loc)
            head_loc[1] = head_loc[1] + 1
            head_loc = tuple(head_loc)
        next_head_loc = tuple(next_head_loc)
    elif direction == 'U':
        next_head_loc = list(head_loc)
        next_head_loc[0] = next_head_loc[0] -1
        if next_head_loc[0] < 0:
            rope_map = np.vstack((np.full((len(rope_map[0])),'.')[np.newaxis,:],rope_map))
            tracking_map = np.vstack((np.zeros((len(tracking_map[0])))[np.newaxis,:],tracking_map))
            next_head_loc[0] = 0
            head_loc = list(head_loc)
            head_loc[0] = head_loc[0] + 1
            head_loc = tuple(head_loc)
        next_head_loc = tuple(next_head_loc)
    elif direction == 'D':
        next_head_loc = list(head_loc)
        next_head_loc[0] = next_head_loc[0] +1
        next_head_loc = tuple(next_head_loc)
        if next_head_loc[0] > len(rope_map)-1:
            rope_map = np.vstack((rope_map , np.full((len(rope_map[0])),'.')[np.newaxis,:]))
            tracking_map = np.vstack((tracking_map,np.zeros((len(tracking_map[0])))[np.newaxis,:]))

    if verbose: print('head moving to: ',next_head_loc)

    tail_loc = list(zip(*np.where(rope_map == '1')))
    if len(tail_loc) != 0:
        tail_loc = tail_loc[0]
    else: tail_loc = head_loc # catch corner case where head is on same space as tail
    if verbose: print('tail at: ',tail_loc)

    #check if tail must be moved
    head_tail_diff = abs(np.subtract(next_head_loc, tail_loc))

    if head_tail_diff[0] > 1 or head_tail_diff[1] > 1:
        next_tail_loc = head_loc
        if verbose: print('Tail moving to: ',next_tail_loc)
        tail_move = True
    else:
        next_tail_loc = tail_loc
        if verbose: print('Tail staying at: ',next_tail_loc)
        tail_move = False

    # reset and update map and tail tracking map
    if len(next_head_loc) > 2:
        if verbose: print(next_head_loc)
        quit()
    rope_map[head_loc] = '.'
    rope_map[tail_locations[8]] = '.'
    rope_map[next_tail_loc] = '1'

    if tail_move:
        for tail in range(len(tail_locations)-1,0,-1):
            if verbose: print('setting tail ',tail+1,' to ', tail_locations[tail-1])
            tail_locations[tail] = tail_locations[tail-1]
            rope_map[tail_locations[tail]] = str(tail+1)
    tail_locations[0] = next_tail_loc
    rope_map[next_head_loc] = 'H'
    tracking_map[tail_locations[8]] = 1
    return rope_map,tracking_map,tail_locations



filename = "./inputs/day9_input.txt"

with open(filename,'r') as f:
    moves = f.read().split('\n')

moves = [line.split() for line in moves]

# set up initial map (will expand as rope head moves)
rope_map = np.full((10,10),'.')
#set starting point
rope_map[-1,0] = 'H'
track = np.zeros_like(rope_map,dtype=int)
starting = tuple([9,0])
tail_locations = [starting]*9
for move in moves:
    if verbose: print(move[0])
    for num_spaces in range(1,int(move[1])+1):
        rope_map,track,tail_locations = move_head(move[0],rope_map,track,tail_locations)
        if verbose: print('moved!')
        if verbose: print(rope_map)
        if verbose: print(track)
    
print('Part 1 - Tail visits ',int(np.sum(track)),' unique spots')