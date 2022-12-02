# function that returns the result of the game + score for player choice
def play_game(throw):
    # 1 - Rock
    # 2 - Paper
    # 3 - Scissors
    opp = int(throw[0])
    player = int(throw[1])
    score = opp - player
    if score == 0: # tie
        result = 3
    elif score == -1 or score == 2: # win
        result = 6
    else:
        result = 0
    
    return result + player

def play_game_for_result(throw):
    # 1 - Rock
    # 2 - Paper
    # 3 - Scissors
    opp = int(throw[0])
    outcome = int(throw[1])

    if outcome == 2: # tie
        player = opp
        result = 3
    elif outcome == 3:
        result = 6
        if opp == 3:
            player = 1
        elif opp == 2:
            player = 3
        else:
            player = 2
    else:
        result = 0
        if opp == 3:
            player = 2
        elif opp == 2:
            player = 1
        else:
            player = 3
    
    return result + player

filename = "./inputs/day2_input.txt"

with open(filename,'r') as f:
    games = f.read().split('\n')

games = [game.replace(' ','')
    .replace('A','1')
    .replace('X','1')
    .replace('B','2')
    .replace('Y','2')
    .replace('C','3')
    .replace('Z','3') for game in games]

print('Part 1: ',sum(map(play_game,games)))
print('Part 2: ',sum(map(play_game_for_result,games)))