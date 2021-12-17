# Advent of Code 2021 Day 17 - Part 1
import math
def processData(string):
    string = string.replace('\n','')
    return string

def calculateTrajectory(velX, velY):
    currX = 0
    currY = 0
    while currY > minY:
        currX += velX
        currY += velY
        if velX > 0:
            velX -= 1
        elif velX < 0:
            velX += 1
        velY -= 1
        if currX >= minX and currX <= maxX and currY >= minY and currY <= maxY:
            return True
    return False   

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

answer = 0
# need to think of a smarter way to retrieve these values...
for x in range(maxX+1):
    for y in range(minY,math.ceil(minX/2)):
        if calculateTrajectory(x,y):
            answer += 1
 
print(answer)
