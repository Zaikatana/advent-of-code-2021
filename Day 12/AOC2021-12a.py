# Advent of Code 2021 Day 12 - Part 1
def processData(string):
    string = string.replace('\n','')
    return string

def generateAdjList(nodes):
    adjList = {}
    for node in nodes:
        splitNode = node.split('-')
        if splitNode[0] not in adjList:
            adjList[splitNode[0]] = [splitNode[1]]
        else:
            adjList[splitNode[0]].append(splitNode[1])
        if splitNode[1] not in adjList:
            adjList[splitNode[1]] = [splitNode[0]]
        else:
            adjList[splitNode[1]].append(splitNode[0])
    return adjList

def dfs(node,adjList,visited,path):
    size = 0
    # return 1 if end is reached
    path += node + ' '
    if node == 'end':
        print(path)
        return 1
    # return 0 if visited
    if node in visited:
        return 0
    # get neighbours
    neighbours = adjList[node]
    # mark visited if not uppercase
    if node.islower():
        visited[node] = True
    # since we want a record of all paths, we have to record the visited nodes for each path
    for neighbour in neighbours:
        altVisited = visited.copy()
        size += dfs(neighbour,adjList,altVisited,path)

    return size

f = open('input.txt', 'r')
nodes = f.readlines()
nodes = list(map(processData, nodes))
f.close()

adjList = generateAdjList(nodes)

print(adjList)
visited = {}

answer = dfs('start',adjList,visited,'')

print(answer)

