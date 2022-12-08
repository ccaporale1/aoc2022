filename = "./inputs/day7_input.txt"

with open(filename,'r') as f:
    lines = f.read().split('\n')

lines = [line.split() for line in lines]

directories = {}
cur_dir = []
for line in lines:
    if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
        new_dir = ''.join(cur_dir) + line[2]
        cur_dir.append(new_dir)
        directories[new_dir] = 0
    elif line[0].isdigit():

        for directory in cur_dir:
            directories[directory] += int(line[0])
    elif line[0] == '$' and line[1] == 'cd' and line[2] == '..':
        
        cur_dir.pop(-1)
    

print('Part 1: ', sum(list(dict(filter(lambda elem: elem[1] <= 100000,directories.items())).values())))
sorted_dirs = dict(sorted(directories.items(), key=lambda item: item[1]))
needed = abs(40000000 - list(sorted_dirs.values())[-1])
print(needed)
for sizes in sorted_dirs.values():
    #print(sizes)
    if sizes > needed:
        print('Part 2: ',sizes)
        break
