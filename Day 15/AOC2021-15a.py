# Advent of Code 2021 Day 15 - Part 1
from queue import PriorityQueue
import sys

def processData(string):
    string = string.replace('\n','')
    return string

# Better way to get neighbours
def getNeighbours(x,y,matrix,cost):
    neighbours = []
    operations = [(0,1),(1,0),(0,-1),(-1,0)]
    for operation in operations:
        xAdd = x+operation[0]
        yAdd = y+operation[1]
        if xAdd >= 0 and xAdd < len(matrix[0]) and yAdd >= 0 and yAdd < len(matrix):
            neighbours.append((cost + matrix[yAdd][xAdd], (xAdd,yAdd)))
    return neighbours

# Utilise Dijkstra with Priority Queue to Find the shortest Path from top left to bottom right
def dijkstra(matrix):
    # Priority queue will automatically sort tuples inserted into queue by cost in ascending order. O(logn) insertion time.
    queue = PriorityQueue()
    queue.put((0, (0,0)))
    # Create a shortest path matrix, utilising Tabulation Dynamic Programming to store the current shortest path for each coordinate
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
            # grab neighbours
            neighbours = getNeighbours(x,y,matrix,cost)
            for neighbour in neighbours:
                neighbourX = neighbour[1][0]
                neighbourY = neighbour[1][1]
                neighbourCost = neighbour[0]
                # If neighbour cost is less than the neighbour cost that exists in the shortest path matrix, append it to priority queue
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
