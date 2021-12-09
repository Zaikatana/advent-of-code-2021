# Advent of Code 2021 Day 9 - Part 1
def processData(string):
    string = string.replace('\n','')
    heightMap = []
    for lines in string:
        heightMap.append(int(lines))
    return heightMap

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# Retrieve Neighbours
def getNeighbours(coord):
    x = coord.x
    y = coord.y
    neighbours = []
    if x == 0 and y == 0:
        neighbours.append(Coordinate(x+1,y))
        neighbours.append(Coordinate(x,y+1))
    elif x == 0 and y == len(heightMap) - 1:
        neighbours.append(Coordinate(x+1,y))
        neighbours.append(Coordinate(x,y-1))
    elif x == len(heightMap[y]) - 1 and y == 0:
        neighbours.append(Coordinate(x-1,y))
        neighbours.append(Coordinate(x,y+1))
    elif x == len(heightMap[y]) - 1 and y == len(heightMap) - 1:
        neighbours.append(Coordinate(x-1,y))
        neighbours.append(Coordinate(x,y-1))
    else:
        if x == 0:
            neighbours.append(Coordinate(x,y+1))
            neighbours.append(Coordinate(x,y-1))
            neighbours.append(Coordinate(x+1,y))
        elif x == len(heightMap[y]) - 1:
            neighbours.append(Coordinate(x-1,y))
            neighbours.append(Coordinate(x,y+1))
            neighbours.append(Coordinate(x,y-1))
        elif y == 0:
            neighbours.append(Coordinate(x+1,y))
            neighbours.append(Coordinate(x-1,y))
            neighbours.append(Coordinate(x,y+1))
        elif y == len(heightMap) - 1:
            neighbours.append(Coordinate(x+1,y))
            neighbours.append(Coordinate(x-1,y))
            neighbours.append(Coordinate(x,y-1))
        else:
            neighbours.append(Coordinate(x-1,y))
            neighbours.append(Coordinate(x+1,y))
            neighbours.append(Coordinate(x,y+1))
            neighbours.append(Coordinate(x,y-1))
    return neighbours

# Depth First Search Function - Essentially traverse neighbours until you reach a visited coordinate/coordinate of height 9
def dfs(coord,visitedMap):
    x = coord.x
    y = coord.y
    size = 0
    c = f'{x}{y}'
    if c in visitedMap:
        return 0
    else:
        visitedMap[c] = True
    if heightMap[y][x] == 9:
        return 0
    else:
        size += 1
        neighbours = getNeighbours(coord)
        for neighbour in neighbours:
            size += dfs(neighbour,visitedMap)
    return size

f = open('input.txt', 'r')
heightMap = f.readlines()
heightMap = list(map(processData, heightMap))
f.close()

# Retrieve coordinates at for the lowest points
lowPoints = []
for y in range(0, len(heightMap)):
    for x in range(0, len(heightMap[y])):
        if x == 0 and y == 0:
            if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y+1][x]:
                lowPoints.append(Coordinate(x,y)) 
        elif x == 0 and y == len(heightMap) - 1:
            if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y-1][x]:
                lowPoints.append(Coordinate(x,y)) 
        elif x == len(heightMap[y]) - 1 and y == 0:
            if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y+1][x]:
                lowPoints.append(Coordinate(x,y)) 
        elif x == len(heightMap[y]) - 1 and y == len(heightMap) - 1:
            if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y-1][x]:
                lowPoints.append(Coordinate(x,y)) 
        else:
            if x == 0:
                if heightMap[y][x] < heightMap[y+1][x] and heightMap[y][x] < heightMap[y-1][x] and heightMap[y][x] < heightMap[y][x+1]:
                    lowPoints.append(Coordinate(x,y)) 
            elif x == len(heightMap[y]) - 1:
                if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y+1][x] and heightMap[y][x] < heightMap[y-1][x]:
                    lowPoints.append(Coordinate(x,y)) 
            elif y == 0:
                if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y+1][x]:
                    lowPoints.append(Coordinate(x,y)) 
            elif y == len(heightMap) - 1:
                if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y-1][x]:
                    lowPoints.append(Coordinate(x,y)) 
            else:
                if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y+1][x] and heightMap[y][x] < heightMap[y-1][x]:
                    lowPoints.append(Coordinate(x,y))

# Use DFS to find the size of all basins
poolSizes = []
for points in lowPoints:
    visitedMap = {}
    size = dfs(points,visitedMap)
    poolSizes.append(size)

# Sort Pool Sizes to find the 3 largest Pools
poolSizes = sorted(poolSizes)
largest = poolSizes[len(poolSizes)-1]
largest2 = poolSizes[len(poolSizes)-2]
largest3 = poolSizes[len(poolSizes)-3]

answer = largest * largest2 * largest3
print(answer)