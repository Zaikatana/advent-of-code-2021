# Advent of Code 2021 Day 12 - Part 1
def processData(string):
    string = string.replace('\n','')
    return string

# Basic function that converts the coordinates into a bidirectional adjacency list graph
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

# Retrieves All Lower Case Values in Adj List
def retrieveLowerCaseValues(dict):
    keys = list(dict.keys())
    lowerCaseValues = []
    for key in keys:
        if key.islower():
            lowerCaseValues.append(key)
    # remove start and end because we always want to traverse these once
    lowerCaseValues.remove('start')
    lowerCaseValues.remove('end')
    return lowerCaseValues

# Traverse through the graph, recording all paths and adding it into the paths set to record all unique paths
def dfs(node,adjList,visited,path,paths):
    # store path to set and return
    path += node + ' '
    if node == 'end':
        paths.add(path)
        print(path)
        return
    # return if visited
    if node in visited:
        if visited[node] == 0:
            return
        else:
            visited[node] -= 1
    # get neighbours
    neighbours = adjList[node]
    # mark node as traversed
    if node.islower():
        if node not in visited:
            visited[node] = 0
    # since we want a record of all paths, we have to record the visited nodes for each path
    for neighbour in neighbours:
        altVisited = visited.copy()
        dfs(neighbour,adjList,altVisited,path,paths)
    return

f = open('input.txt', 'r')
nodes = f.readlines()
nodes = list(map(processData, nodes))
f.close()

adjList = generateAdjList(nodes)
lowerCaseValues = retrieveLowerCaseValues(adjList)
paths = set()

# perform dfs, but we submit a visited map that has permits 1 small cave to be explored twice
for lc in lowerCaseValues:
    visited = {}
    visited[lc] = 2
    dfs('start',adjList,visited,'',paths)

answer = len(paths)
print(answer)
