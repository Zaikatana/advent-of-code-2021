# Advent of Code 2021 Day 14 - Part 1
def processData(string):
    string = string.replace('\n','')
    return string

def processInsertionRules(data):
    rules = {}
    for line in data:
        sLine = line.split(' -> ')
        rules[sLine[0]] = sLine[1]
    return rules

f = open('input.txt', 'r')
data = f.readlines()
data = list(map(processData, data))
f.close()

polymerTemplate = data[0]
insertionRules = processInsertionRules(data[2:])

for i in range(0,10):
    newPolymerTemplate = ''
    for j in range(0,len(polymerTemplate)):
        if j == len(polymerTemplate) - 1:
            pair = polymerTemplate[j]
        else:
            pair = polymerTemplate[j:j+2]
        if pair in insertionRules:
            newPolymerTemplate += f'{pair[0]}{insertionRules[pair]}'
        else:
            newPolymerTemplate += pair
    polymerTemplate = newPolymerTemplate

frequencyMap = {}
for c in polymerTemplate:
    if c in frequencyMap:
        frequencyMap[c] += 1
    else:
        frequencyMap[c] = 1

maxCount = frequencyMap[polymerTemplate[0]]
minCount = frequencyMap[polymerTemplate[0]]
for key in frequencyMap.keys():
    maxCount = max(maxCount,frequencyMap[key])
    minCount = min(minCount,frequencyMap[key])

answer = maxCount - minCount
print(answer)
