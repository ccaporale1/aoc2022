import QLearner as ql
import numpy as np

verbose = False
with open('./inputs/day12_input.txt') as f:
    heightmap = f.read().split('\n')
heightmap = np.array(heightmap)
row_len = len(heightmap[0])
map_height = len(heightmap)
heightmap_flat = heightmap.flatten()
heightmap_states = list("".join([str(item) for item in heightmap_flat]))
pit_track = 0
# create Qlearner
# num_states = number of locations on heightmap => num_rows(heightmap) * length of row
# num_actions = 4 => up = 0 , down = 1, left = 2, right = 3
learner = ql.QLearner(
    num_states=map_height*row_len,
    num_actions=4,
    alpha=0.7,
    gamma=0.2,
    rar=0.95,
    radr=0.99,
    dyna=0,
    verbose=False)
epochs = 1000

def descritize(loc):
    if loc < row_len:
        return (0,loc)
    else:
        return divmod(loc,row_len)

def check_letter_diff(letter1,letter2):
    if letter1 == 'z' and letter2 == 'E':
        return True
    elif letter1 != 'S':
        check = abs(ord(letter1)-ord(letter2)) <= 1
        if verbose: print('Letter check result for ',letter1, ' and ',letter2,' is ',check)
    else:
        check = True
    return check

def get_reward (letter1,letter2):
   
    if letter2 == 'S':
        return -10
    elif ord(letter1) < ord(letter2) and letter2 != 'S':
        return -1
    elif ord(letter1) > ord(letter2):
        return -2.5
    else: return -2

def move(action,state):
    
    state_coord = descritize(state)
    if verbose: print('Moving from state: ',state_coord)
    
    if int(action) == 0: #up
        new_state = state-row_len
        new_state_coord = descritize(new_state)
        if verbose: print('Moving UP to state: ',new_state_coord)
        if state_coord[0] == 0 or not check_letter_diff(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]]): #cant go up!!!
            if verbose: print('JK - cant do that!!')
            return state,-10
        else:
            #heightmap[state_coord[0],state_coord[1]] = '^'
            return new_state,get_reward(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]])
    elif int(action) == 1: # down
        new_state = state+row_len
        new_state_coord = descritize(new_state)
        if verbose: print('Moving DOWN to state: ',new_state_coord)
        if state_coord[0] == map_height-1 or not check_letter_diff(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]]): #cant go down!!!
            if verbose: print('JK - cant do that!!')
            return state,-10
        else:
            #heightmap[state_coord[0],state_coord[1]] = '_'
            return new_state,get_reward(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]])
    elif int(action) == 2: #left
        new_state = state-1
        new_state_coord = descritize(new_state)
        if verbose: print('Moving LEFT to state: ',new_state_coord)
        if state_coord[1] == 0 or not check_letter_diff(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]]): # cant go left!!
            if verbose: print('JK - cant do that!!')
            return state,-10
        else:
            # heightmap[state_coord[0],state_coord[1]] = '<'
            return new_state,get_reward(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]])
    elif int(action) == 3: #right
        new_state = state+1
        new_state_coord = descritize(new_state)
        if verbose: print('Moving RIGHT to state: ',new_state_coord)
        if state_coord[1] == row_len-1 or not check_letter_diff(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]]): #cant go right!!!
            if verbose: print('JK - cant do that!!')
            return state,-10
        else:
            #heightmap[state_coord[0],state_coord[1]] = '>'
            return new_state,get_reward(heightmap[state_coord[0]][state_coord[1]],heightmap[new_state_coord[0]][new_state_coord[1]])
last_steps = 0
for i in range(0,epochs):

    location = heightmap_states.index('S')
    if verbose: print('Starting location is: ', location)
    action = learner.querysetstate(location)
    if verbose: print('Starting action is: ', action)
    steps = 0
    while heightmap_states[location] != 'E': #continue until goal is reached
        location,r = move(action,location)
        #print(heightmap_states[location] )
        if heightmap_states[location] == 'E':
            r = 1
        
        action = learner.query(location,r)
        steps += 1
        if steps > 100000: break
    print(steps)
    print('Last spot = ',descritize(location))
    if steps == last_steps and steps < 1000:
        break
    else: last_steps = steps




if verbose: 
    for row in heightmap:
        for i, pixel in enumerate(row):
            print(pixel, end="")
            
        print("\n", end="")