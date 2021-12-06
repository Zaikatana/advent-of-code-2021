# Advent of Code 2021 Day  - Part 1
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

# Brute Force Method, takes much longer than method used in part B, as array grows exponentially
for i in range(0,80):
    for j in range(0,len(initialState)):
        if initialState[j] == 0:
            initialState[j] = 6
            initialState.append(8)
        else:
            initialState[j] -= 1
print(len(initialState))