import numpy as np

verbose = False
filename = "./inputs/day8_input.txt"

with open(filename,'r') as f:
    lines = f.read().split('\n')

lines = [*lines]
for line in range(0,len(lines)):
    lines[line] = [*lines[line]]

tree_map = np.array(lines)
num_vis = 0
tree_scores = np.zeros_like(tree_map,dtype=int)
for row in range(1,len(tree_map)-1):

    for col in range(1,len(tree_map[row])-1):
        
        num_up= 0
        num_down= 0
        num_right= 0
        num_left = 0
        vis_flag = [True,True,True,True] 
        curr_tree = tree_map[row][col]
        trees_up = tree_map[row-1::-1,col] 
        trees_down = tree_map[row+1::,col]
        trees_left = tree_map[row,col-1::-1]
        trees_right = tree_map[row,col+1::]
        if verbose: print('up - ',trees_up,' down -',trees_down,' left -',trees_left,' right -',trees_right)
        for compare in range(0,len(trees_up)):
            if verbose:print('up - comparing tree ',curr_tree,' with tree ',trees_up[compare])
            num_up +=1
            if curr_tree <= trees_up[compare][0]:
                vis_flag[0] = False
            
                break

        for compare in range(0,len(trees_down)):
            if verbose:print('down - comparing tree ',curr_tree,' with tree ',trees_down[compare])
            num_down +=1
            if curr_tree <= trees_down[compare]:
                vis_flag[1] = False
                break
        for compare in range(0,len(trees_left)):
            if verbose:print('left - comparing tree ',curr_tree,' with tree ',trees_left[compare])
            num_left +=1
            if curr_tree <= trees_left[compare]:
                vis_flag[2] = False
    
                break
    
        for compare in range(0,len(trees_right)):
            if verbose:print('right - comparing tree ',curr_tree,' with tree ',trees_right[compare])
            num_right +=1 
            if curr_tree <= trees_right[compare]:
                vis_flag[3] = False
                
                break
      
        tree_scores[row,col] = num_up * num_down * num_right * num_left  
        if verbose:print(row,col)
        if verbose:print(num_up , num_down , num_right,num_left  )
        if any(vis_flag):
            num_vis += 1
num_vis = num_vis + len(tree_map[0])*2 + (len(tree_map)-2)*2
print('Part 1 - Number of visible trees: ',num_vis)

print('Part 2 - Tree Visibility Score: ',tree_scores[np.unravel_index(np.argmax(tree_scores), tree_scores.shape)])
if verbose:print(tree_scores)