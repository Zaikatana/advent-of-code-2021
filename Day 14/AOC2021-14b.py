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
pairFrequency = {}
frequencyMap = {}
for c in polymerTemplate:
    if c in frequencyMap:
        frequencyMap[c] += 1
    else:
        frequencyMap[c] = 1

for j in range(0,len(polymerTemplate) - 1):
    pair = polymerTemplate[j:j+2]
    if pair in pairFrequency:
        pairFrequency[pair] += 1
    else:
        pairFrequency[pair] = 1

for i in range(0,40):
    # process pairs
    keys = list(pairFrequency.keys()).copy()
    values = list(pairFrequency.values()).copy()
    for j in range(len(keys)):
        # turn pair into 2 pairs
        pairA = f'{keys[j][0]}{insertionRules[keys[j]]}'
        pairB = f'{insertionRules[keys[j]]}{keys[j][1]}'
        # add pairs into pairFrequency
        if pairA in pairFrequency:
            pairFrequency[pairA] += values[j]
        else:
            pairFrequency[pairA] = values[j]
        if pairB in pairFrequency:
            pairFrequency[pairB] += values[j]
        else:
            pairFrequency[pairB] = values[j]
        # perform appropriate subtractions
        pairFrequency[keys[j]] -= values[j]
        # add in frequency
        if insertionRules[keys[j]] in frequencyMap:
            frequencyMap[insertionRules[keys[j]]] += values[j]
        else:
            frequencyMap[insertionRules[keys[j]]] = values[j]

maxCount = frequencyMap[polymerTemplate[0]]
minCount = frequencyMap[polymerTemplate[0]]
for key in frequencyMap.keys():
    maxCount = max(maxCount,frequencyMap[key])
    minCount = min(minCount,frequencyMap[key])

answer = maxCount - minCount
print(answer)