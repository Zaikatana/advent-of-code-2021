# Advent of Code 2021 Day 13 - Part 2
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Command:
    def __init__(self,axis,pos):
        self.axis = axis
        self.pos = pos

def processData(string):
    string = string.replace('\n','')
    return string

def createGraph(data):
    coordinates = []
    maxX = 0
    maxY = 0
    for line in data:
        if line == '':
            break
        else:
            l = line.split(',')
            x = int(l[0])
            y = int(l[1])
            coordinates.append(Coordinate(x,y))
            maxX = max(maxX,x)
            maxY = max(maxY,y)
    maxX += 1
    maxY += 1
    graph = [['.']*maxX for _ in range(maxY)]
    for coord in coordinates:
        graph[coord.y][coord.x] = '#'
    return graph
    
def retrieveCommands(data):
    commands = []
    for line in data:
        if len(line) > 13:
            l = line.split(' ')
            axis = l[2][0]
            pos = int(l[2][2:])
            commands.append(Command(axis,pos))
    return commands

def countDots(graph):
    dots = 0
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] == '#':
                dots += 1
    return dots

def fold(command,graph):
    axis = command.axis
    pos = command.pos
    newGraph = []
    graphA = []
    graphB = []
    if axis == 'y':
        graphA = graph[0:pos]
        graphB = list(reversed(graph[pos+1:]))
    else:
        for y in range(len(graph)):
            graphA.append(graph[y][0:pos])
            graphB.append(list(reversed(graph[y][pos+1:])))
    newGraph = combine(graphA,graphB)
    return newGraph

# Merge 2 arrays together
def combine(graphA,graphB):
    graphALen = len(graphA) * len(graphA[0])
    graphBLen = len(graphB) * len(graphB[0])
    diffX = abs(len(graphA[0]) - len(graphB[0]))
    diffY = abs(len(graphA) - len(graphB))
    if graphALen >= graphBLen:
        bigGraph = graphA
        littleGraph = graphB
    else:
        bigGraph = graphB
        littleGraph = graphA
    for y in range(len(littleGraph)):
        for x in range(len(littleGraph[y])):
            if littleGraph[y][x] == '#':
                bigGraph[diffY+y][diffX+x] = '#'
    return bigGraph

f = open('input.txt', 'r')
data = f.readlines()
data = list(map(processData, data))
f.close()

graph = createGraph(data)
commands = retrieveCommands(data)
for command in commands:
    graph = fold(command,graph)
print(graph)