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

# Better way to get neighbours
def getNeighbours(coord,octopi):
    neighbours = []
    operations = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for operation in operations:
        xAdd = coord.x+operation[0]
        yAdd = coord.y+operation[1]
        if xAdd >= 0 and xAdd < len(octopi[0]) and yAdd >= 0 and yAdd < len(octopi):
            neighbours.append(Coordinate(xAdd,yAdd))
    return neighbours

def flash(coord, octopi):
    x = coord.x
    y = coord.y
    neighbours = getNeighbours(coord,octopi)
    for neighbour in neighbours:
        octopi[neighbour.y][neighbour.x] += alreadyFlashed(octopi[neighbour.y][neighbour.x])

f = open('input.txt', 'r')
octopi = f.readlines()
octopi = list(map(processData, octopi))
f.close()

answer = 0

flashCount = 0
step = 0
while flashCount != len(octopi)*len(octopi[0]):
    flashCount = 0
    octopi = list(map(addOneToList, octopi))
    while True:
        allFlashed = True
        for j in range(0, len(octopi)):
            for k in range(0, len(octopi[j])):
                if octopi[j][k] > 9:
                    octopi[j][k] = 0
                    flash(Coordinate(k,j),octopi)
                    flashCount += 1
        # Search for any remaining values > 9 post flash
        for l in range(0, len(octopi)):
            for m in range(0, len(octopi[l])):
                if octopi[l][m] > 9:
                    allFlashed = False
        if allFlashed:
            break
    step += 1

print(step)
