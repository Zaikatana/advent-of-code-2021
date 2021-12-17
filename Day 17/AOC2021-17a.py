# Advent of Code 2021 Day 17 - Part 1
import math
def processData(string):
    string = string.replace('\n','')
    return string

def calculateTrajectory(velX, velY):
    currX = 0
    currY = 0
    highestY = 0
    while True:
        currX += velX
        currY += velY
        highestY = max(currY,highestY)
        if velX > 0:
            velX -= 1
        elif velX < 0:
            velX += 1
        velY -= 1
        if currX >= minX and currX <= maxX and currY >= minY and currY <= maxY:
            return highestY
        if currY < minY:
            return 0       

f = open('input.txt', 'r')
data = f.readline()
data = processData(data)
f.close()

data = data[15:]
data = data.split(', y=')
minX = int(data[0].split('..')[0])
maxX = int(data[0].split('..')[1])
minY = int(data[1].split('..')[0])
maxY = int(data[1].split('..')[1])

maxValues = []
# need to think of a smarter way to retrieve these values...
for x in range(math.ceil(minX/2)):
    for y in range(math.ceil(minX/2)):
        maxValues.append(calculateTrajectory(x,y))
answer = max(maxValues)
print(answer)
