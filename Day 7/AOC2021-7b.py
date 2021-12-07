# Advent of Code 2021 Day 7 - Part 2
def removeNewLine(string):
    string = string.replace('\n','')
    horizontalPositions = string.split(',')
    intPos = []
    for pos in horizontalPositions:
        intPos.append(int(pos))
    return intPos

f = open('input.txt', 'r')
horizontalPositions = f.readlines()
horizontalPositions = list(map(removeNewLine, horizontalPositions))
horizontalPositions = horizontalPositions[0]
f.close()

# generate count dict to retrieve unique items
count = {}

for pos in horizontalPositions:
    if pos not in count:
        count[pos] = 1
    else:
        count[pos] += 1

# 1 + 2 + ... + n = n(n+1)/2
fuel = 0
for pos in count.keys():
    posFuel = 0
    for hp in horizontalPositions:
        difference = abs(hp - pos)
        posFuel += ((difference + 1) * difference)/2
    if fuel == 0:
        fuel = posFuel
    else:
        fuel = min(fuel, posFuel)

print(int(fuel))

