# Advent of Code 2021 Day 9 - Part 1
def processData(string):
    string = string.replace('\n','')
    heightMap = []
    for lines in string:
        heightMap.append(int(lines))
    return heightMap

def addOne(num):
    return num + 1

f = open('input.txt', 'r')
heightMap = f.readlines()
heightMap = list(map(processData, heightMap))
f.close()

lowPoints = []

for y in range(0, len(heightMap)):
    for x in range(0, len(heightMap[y])):
        if x == 0 and y == 0:
            if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y+1][x]:
                lowPoints.append(heightMap[y][x]) 
        elif x == 0 and y == len(heightMap) - 1:
            if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y-1][x]:
                lowPoints.append(heightMap[y][x]) 
        elif x == len(heightMap[y]) - 1 and y == 0:
            if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y+1][x]:
                lowPoints.append(heightMap[y][x]) 
        elif x == len(heightMap[y]) - 1 and y == len(heightMap) - 1:
            if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y-1][x]:
                lowPoints.append(heightMap[y][x]) 
        else:
            if x == 0:
                if heightMap[y][x] < heightMap[y+1][x] and heightMap[y][x] < heightMap[y-1][x] and heightMap[y][x] < heightMap[y][x+1]:
                    lowPoints.append(heightMap[y][x]) 
            elif x == len(heightMap[y]) - 1:
                if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y+1][x] and heightMap[y][x] < heightMap[y-1][x]:
                    lowPoints.append(heightMap[y][x]) 
            elif y == 0:
                if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y+1][x]:
                    lowPoints.append(heightMap[y][x]) 
            elif y == len(heightMap) - 1:
                if heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y-1][x]:
                    lowPoints.append(heightMap[y][x]) 
            else:
                if heightMap[y][x] < heightMap[y][x-1] and heightMap[y][x] < heightMap[y][x+1] and heightMap[y][x] < heightMap[y+1][x] and heightMap[y][x] < heightMap[y-1][x]:
                    lowPoints.append(heightMap[y][x])
lowPoints = list(map(addOne, lowPoints))
answer = sum(lowPoints)
print(answer)
