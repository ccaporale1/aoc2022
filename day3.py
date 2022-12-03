import os

def splitStringInHalf(stringToSplit):
    first, second = stringToSplit[:len(stringToSplit)//2], stringToSplit[len(stringToSplit)//2:]
    return {        'firstHalf': first,        'secondHalf': second,    }

def findSharedStrings(dictToCompare):

    return ''.join(set(dictToCompare['firstHalf']).intersection(dictToCompare['secondHalf']))

def compareGroup(listOfElves):
    return ''.join(set(listOfElves[0]).intersection(listOfElves[1]).intersection(listOfElves[2]))

def scoreChar(char):
    if char != '' and char.islower() :
        return ord(char)-96
    elif char != '' and char.isupper() :
        return ord(char)-38
    else:
        return 0

filename = "./inputs/day3_input.txt"

with open(filename,'r') as f:
    packs = f.read().split('\n')

splitPacks = list(map(splitStringInHalf,packs))
commonChars = list(map(findSharedStrings,splitPacks))
scores = list(map(scoreChar,commonChars))
print('Part 1: ',sum(scores))

elfGroups = [packs[i:i+3] for i in range(0,len(packs), 3)]
commonBadges = list(map(compareGroup,elfGroups))
badgeScores = list(map(scoreChar,commonBadges))
print('Part 2: ',sum(badgeScores))