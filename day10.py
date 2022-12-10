import numpy as np
verbose = True
with open('./inputs/day10_input.txt') as f:
    data = f.read().split('\n')
data_part2 = data.copy()

for line in range(0,len(data)):
    data[line] = data[line].split()
    if data[line][0] == 'noop':
        data[line] = 0
    else: data[line] = int(data[line][1])

data = np.array(data)
data = np.insert(data,0,1)
final = np.ones((1,1))

for line in range(1,len(data)):

    if data[line] == 0:
        final = np.append(final,data[line])
    else:

        final = np.append(final,0)
        final = np.append(final,data[line])

sum_data = np.cumsum(final)

print('Part 1 - sum of signal strengths: ',int(sum_data[19]*20+sum_data[59]*60+sum_data[99]*100+sum_data[139]*140+sum_data[179]*180+sum_data[219]*220))

screen_width = 40
CRT = [["." for _ in range(screen_width)] for _ in range(6)]

def pixel () :
    row,col = divmod(cycle,screen_width)
    if col in (x - 1, x, x + 1):
            try:
                CRT[row][col] = "#"
            except IndexError:
                pass

cycle = 0
x = 1

for line in range(0,len(data_part2)):
    point = data_part2[line].split()
    pixel()
    if point[0] == 'noop':
        cycle += 1
    else:
        cycle += 1
        pixel()
        cycle += 1
        x += int(point[1])

pixel()

# draw screen
for row in CRT:
    for i, pixel in enumerate(row):
        print(pixel, end="")
        if i == 39:
            print("\n", end="")