filename = "./inputs/day6_input.txt"

with open(filename,'r') as f:
    transmission = f.read()

lastfour = list(transmission[0:3])
rest = list(transmission[3::])
num_processed = 3
for letter in rest:
    lastfour += letter
    check_set = set(lastfour)
    num_processed += 1
    if len(check_set) != 4:
        lastfour.pop(0)
        
    else:
        break

print('Part 1: ',num_processed)

lastfourteen = list(transmission[0:13])
rest = list(transmission[13::])

num_processed = 13
for letter in rest:
    lastfourteen += letter
    check_set = set(lastfourteen)
    num_processed += 1
    if len(check_set) != 14:
        lastfourteen.pop(0)
        
    else:
        break

print('Part 2: ',num_processed)
