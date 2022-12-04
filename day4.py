def process_pairs_contain(pair):
    one_split = pair[0].split('-')
    two_split = pair[1].split('-')

    if int(one_split[0]) <= int(two_split[0]) and int(one_split[1]) >= int(two_split[1]):
        return 1
    elif int(one_split[0]) >= int(two_split[0]) and int(one_split[1]) <= int(two_split[1]):
        return 1
    else:
        return 0

def process_pairs_overlap(pair):
    one_split = pair[0].split('-')
    two_split = pair[1].split('-')

    if int(one_split[0]) <= int(two_split[0]) and int(one_split[1]) >= int(two_split[0]):
        return 1
    elif int(one_split[0]) >= int(two_split[0]) and int(one_split[0]) <= int(two_split[1]):
        return 1
    elif int(one_split[0]) <= int(two_split[1]) and int(one_split[1]) >= int(two_split[1]):
        return 1
    elif int(one_split[1]) >= int(two_split[0]) and int(one_split[1]) <= int(two_split[1]):
        return 1
    else:
        return 0

filename = "./inputs/day4_input.txt"

with open(filename,'r') as f:
    pairs = f.read().split('\n')

split_pairs = []
for pair in pairs:
    split_pairs.append(pair.split(','))

print('Part 1: ', sum(list(map(process_pairs_contain,split_pairs))))
print('Part 2: ', sum(list(map(process_pairs_overlap,split_pairs))))