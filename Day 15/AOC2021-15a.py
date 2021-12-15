# Advent of Code 2021 Day 15 - Part 1
from queue import PriorityQueue
import sys

def processData(string):
    string = string.replace('\n','')
    return string

def dijkstra(matrix):
    queue = PriorityQueue()
    queue.put((0, (0,0)))
    spMatrix = [[sys.maxsize]*len(matrix[0]) for _ in range(len(matrix))]
    while not queue.empty():
        coord = queue.get()
        x = coord[1][0]
        y = coord[1][1]
        cost = coord[0]
        if x == 0 and y == 0:
            spMatrix[y][x] = 0
        if x == len(matrix[0]) - 1 and y == len(matrix) - 1:
            spMatrix[y][x] = cost
            break
        else:
            # grab neighbours... need to find a cleaner way of doing this in python
            neighbours = []
            if x == 0 and y == 0:
                neighbours.append((cost+matrix[y][x+1], (x+1,y)))  
                neighbours.append((cost+matrix[y+1][x], (x,y+1)))
            elif x == 0 and y == len(matrix) - 1:
                neighbours.append((cost+matrix[y][x+1], (x+1,y)))  
                neighbours.append((cost+matrix[y-1][x], (x,y-1)))
            elif x == len(matrix[0]) - 1 and y == 0:
                neighbours.append((cost+matrix[y+1][x], (x,y+1)))
                neighbours.append((cost+matrix[y][x-1], (x-1,y)))
            elif x == 0:
                neighbours.append((cost+matrix[y][x+1], (x+1,y)))  
                neighbours.append((cost+matrix[y+1][x], (x,y+1)))
                neighbours.append((cost+matrix[y-1][x], (x,y-1)))
            elif y == 0:
                neighbours.append((cost+matrix[y][x+1], (x+1,y)))  
                neighbours.append((cost+matrix[y+1][x], (x,y+1)))
                neighbours.append((cost+matrix[y][x-1], (x-1,y)))
            elif x == len(matrix[0]) - 1:
                neighbours.append((cost+matrix[y+1][x], (x,y+1)))
                neighbours.append((cost+matrix[y-1][x], (x,y-1)))
                neighbours.append((cost+matrix[y][x-1], (x-1,y)))
            elif y == len(matrix) - 1:
                neighbours.append((cost+matrix[y][x+1], (x+1,y)))
                neighbours.append((cost+matrix[y-1][x], (x,y-1)))
                neighbours.append((cost+matrix[y][x-1], (x-1,y)))
            else:
                neighbours.append((cost+matrix[y][x+1], (x+1,y)))  
                neighbours.append((cost+matrix[y+1][x], (x,y+1)))
                neighbours.append((cost+matrix[y-1][x], (x,y-1)))
                neighbours.append((cost+matrix[y][x-1], (x-1,y)))
            for neighbour in neighbours:
                neighbourX = neighbour[1][0]
                neighbourY = neighbour[1][1]
                neighbourCost = neighbour[0]
                if spMatrix[neighbourY][neighbourX] > neighbourCost:
                    spMatrix[neighbourY][neighbourX] = neighbourCost
                    queue.put(neighbour)
    return spMatrix[len(matrix) - 1][len(matrix[0]) - 1]

f = open('input.txt', 'r')
data = f.readlines()
data = list(map(processData, data))
f.close()

matrix = []
for lines in data:
    line = []
    for c in lines:
        line.append(int(c))
    matrix.append(line)
answer = dijkstra(matrix)
print(answer)
