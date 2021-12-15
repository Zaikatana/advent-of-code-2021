# Advent of Code 2021 Day 15 - Part 1
from queue import PriorityQueue
import sys

def processData(string):
    string = string.replace('\n','')
    return string

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
                # If neighbour cost is less than the neighbour cost that exists in the shortest path matrix, append it to priority queue
                if spMatrix[neighbourY][neighbourX] > neighbourCost:
                    spMatrix[neighbourY][neighbourX] = neighbourCost
                    queue.put(neighbour)
    return spMatrix[len(matrix) - 1][len(matrix[0]) - 1]

# Add Num to each value in Matrix
def addMatrix(matrix,num):
    if num == 0:
        return matrix.copy()
    newMatrix = []
    for y in range(len(matrix)):
        newMatrixRow = []
        for x in range(len(matrix[0])):
            total = matrix[y][x] + num
            if total > 9:
                total = 1 + ((total-1) - 9)
            newMatrixRow.append(total)
        newMatrix.append(newMatrixRow)
    return newMatrix

# Generate the big Matrix
def generateMatrix(matrix):
    bigMatrix = []
    for i in range(5):
        matrixA = addMatrix(matrix.copy(),i)
        matrixB = addMatrix(matrix.copy(),i+1)
        matrixC = addMatrix(matrix.copy(),i+2)
        matrixD = addMatrix(matrix.copy(),i+3)
        matrixE = addMatrix(matrix.copy(),i+4)
        for j in range(len(matrix)):
            bigMatrix.append(matrixA[j]+matrixB[j]+matrixC[j]+matrixD[j]+matrixE[j])
    return bigMatrix

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
bigMatrix = generateMatrix(matrix)
answer = dijkstra(bigMatrix)
print(answer)
