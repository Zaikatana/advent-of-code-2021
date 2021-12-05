# Advent of Code 2021 Day 5 - Part 1
def removeNewLine(string):
    string = string.replace('\n','')
    string = string.split(' -> ')
    coordinates = []
    for coord in string:
        coordinates += coord.split(',')
    # return list [x1,y1,x2,y2]
    return coordinates

f = open('input.txt', 'r')
coordinates = f.readlines()
coordinates = list(map(removeNewLine, coordinates))
f.close()

maxX = 0
maxY = 0

for coord in coordinates:
    maxCoordX = max(int(coord[0]), int(coord[2]))
    maxCoordY = max(int(coord[1]), int(coord[3]))
    maxX = max(maxX, maxCoordX)
    maxY = max(maxY, maxCoordY)

maxX += 1
maxY += 1
graph = [[0]*maxX for _ in range(maxY)]

for coord in coordinates:
    if coord[0] == coord[2]:
        x = int(coord[0])
        startY = min(int(coord[1]), int(coord[3]))
        endY = max(int(coord[1]), int(coord[3]))
        for y in range(startY,endY+1):
            graph[y][x] += 1
    if coord[1] == coord[3]:
        y = int(coord[1])
        startX = min(int(coord[0]), int(coord[2]))
        endX = max(int(coord[0]), int(coord[2]))
        for x in range(startX,endX+1):
            graph[y][x] += 1

answer = 0

for coord in graph:
    for value in coord:
        if value >= 2:
            answer += 1

print(answer)


    