# Advent of Code 2021 Day 11 - Part 1
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def processData(string):
    string = string.replace('\n','')
    octopi = []
    for lines in string:
        octopi.append(int(lines))
    return octopi

def addOneToList(numList):
    newList = []
    for num in numList:
        newList.append(num+1)
    return newList

def alreadyFlashed(num):
    if num == 0:
        return 0
    else:
        return 1

def flash(coord, octopi):
    x = coord.x
    y = coord.y
    if x == 0 and y == 0:
        octopi[y][x+1] += alreadyFlashed(octopi[y][x+1])
        octopi[y+1][x+1] += alreadyFlashed(octopi[y+1][x+1])
        octopi[y+1][x] += alreadyFlashed(octopi[y+1][x])
    elif x == 0 and y == len(octopi) - 1:
        octopi[y][x+1] += alreadyFlashed(octopi[y][x+1])
        octopi[y-1][x] += alreadyFlashed(octopi[y-1][x])
        octopi[y-1][x+1] += alreadyFlashed(octopi[y-1][x+1])
    elif x == len(octopi[y]) - 1 and y == 0:
        octopi[y][x-1] += alreadyFlashed(octopi[y][x-1])
        octopi[y+1][x] += alreadyFlashed(octopi[y+1][x])
        octopi[y+1][x-1] += alreadyFlashed(octopi[y+1][x-1])
    elif x == len(octopi[y]) - 1 and y == len(octopi) - 1:
        octopi[y][x-1] += alreadyFlashed(octopi[y][x-1])
        octopi[y-1][x] += alreadyFlashed(octopi[y-1][x])
        octopi[y-1][x-1] += alreadyFlashed(octopi[y-1][x-1])
    else:
        if x == 0:
            octopi[y+1][x] += alreadyFlashed(octopi[y+1][x])
            octopi[y-1][x] += alreadyFlashed(octopi[y-1][x])
            octopi[y][x+1] += alreadyFlashed(octopi[y][x+1])
            octopi[y-1][x+1] += alreadyFlashed(octopi[y-1][x+1])
            octopi[y+1][x+1] += alreadyFlashed(octopi[y+1][x+1])
        elif x == len(octopi[y]) - 1:
            octopi[y+1][x] += alreadyFlashed(octopi[y+1][x])
            octopi[y-1][x] += alreadyFlashed(octopi[y-1][x])
            octopi[y][x-1] += alreadyFlashed(octopi[y][x-1])
            octopi[y-1][x-1] += alreadyFlashed(octopi[y-1][x-1])
            octopi[y+1][x-1] += alreadyFlashed(octopi[y+1][x-1])
        elif y == 0:
            octopi[y][x+1] += alreadyFlashed(octopi[y][x+1])
            octopi[y][x-1] += alreadyFlashed(octopi[y][x-1])
            octopi[y+1][x] += alreadyFlashed(octopi[y+1][x])
            octopi[y+1][x+1] += alreadyFlashed(octopi[y+1][x+1])
            octopi[y+1][x-1] += alreadyFlashed(octopi[y+1][x-1])
        elif y == len(octopi) - 1:
            octopi[y][x-1] += alreadyFlashed(octopi[y][x-1])
            octopi[y][x+1] += alreadyFlashed(octopi[y][x+1])
            octopi[y-1][x-1] += alreadyFlashed(octopi[y-1][x-1])
            octopi[y-1][x+1] += alreadyFlashed(octopi[y-1][x+1])
            octopi[y-1][x] += alreadyFlashed(octopi[y-1][x])
        else:
            octopi[y][x-1] += alreadyFlashed(octopi[y][x-1])
            octopi[y][x+1] += alreadyFlashed(octopi[y][x+1])
            octopi[y-1][x-1] += alreadyFlashed(octopi[y-1][x-1])
            octopi[y-1][x+1] += alreadyFlashed(octopi[y-1][x+1])
            octopi[y-1][x] += alreadyFlashed(octopi[y-1][x])
            octopi[y+1][x-1] += alreadyFlashed(octopi[y+1][x-1])
            octopi[y+1][x+1] += alreadyFlashed(octopi[y+1][x+1])
            octopi[y+1][x] += alreadyFlashed(octopi[y+1][x])

f = open('input.txt', 'r')
octopi = f.readlines()
octopi = list(map(processData, octopi))
f.close()

answer = 0

for i in range(0,100):
    octopi = list(map(addOneToList, octopi))
    while True:
        allFlashed = True
        for j in range(0, len(octopi)):
            for k in range(0, len(octopi[j])):
                if octopi[j][k] > 9:
                    octopi[j][k] = 0
                    flash(Coordinate(k,j),octopi)
                    answer += 1
        # Search for any remaining values > 9 post flash
        for l in range(0, len(octopi)):
            for m in range(0, len(octopi[l])):
                if octopi[l][m] > 9:
                    allFlashed = False
        if allFlashed:
            break

print(answer)
