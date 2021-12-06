# Advent of Code 2021 Day  - Part 2
def removeNewLine(string):
    string = string.replace('\n','')
    initialState = string.split(',')
    intStates = []
    for state in initialState:
        intStates.append(int(state))
    return intStates

f = open('input.txt', 'r')
initialState = f.readlines()
initialState = list(map(removeNewLine, initialState))
initialState = initialState[0]
f.close()

count = {}
# initialise count dict
for i in range(0, 9):
    count[i] = 0

# create frequencies
for state in initialState:
    count[state] += 1

# perform logic to modify frequency as day increases
for j in range(0, 256):
    originalCount = list(count.values())
    for k in range(0,9):
        if k == 6:
            count[k] = originalCount[k+1] + originalCount[0]
        elif k == 8:
            count[k] = originalCount[0]
        else:
            count[k] = originalCount[k+1]

values = list(count.values())
sum = 0
for v in values:
    sum += v

print(sum)

