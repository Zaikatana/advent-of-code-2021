# Advent of Code 2021 Day 4 - Part 1
def removeNewLine(string):
    return string.replace('\n','')

# Extracts each Bingo Sheet and adds them to a list
def convertTo3DArray(bingoData):
    arr = []
    twoDArr = []
    for line in bingoData:
        if len(line) == 0:
            arr.append(twoDArr)
            twoDArr = []
        else:
            bingoLine = line.split(' ')
            if len(bingoLine) > 5:
                while(bingoLine.count('')):
                    bingoLine.remove('')
            twoDArr.append(bingoLine)
    return arr

f = open('input.txt', 'r')
bingoData = f.readlines()
f.close()
bingoData = list(map(removeNewLine, bingoData))

bingoCall = bingoData[0].split(',')

bingoData = bingoData[2:len(bingoData)]
bingoData = convertTo3DArray(bingoData)

marked = ['X'] * 5
winningSheet = []
winningNumber = None

# mark of bingo numbers with X for each number, terribly unoptimised since its O(n^4)
for num in bingoCall:
    for bingoSheet in bingoData:
        for bingoRow in bingoSheet:
            if num in bingoRow:
                bingoRow[bingoRow.index(num)] = 'X'
                break
        # determine if any rows or columns is just X
        bingoCol0 = [bingoSheet[0][0], bingoSheet[1][0], bingoSheet[2][0], bingoSheet[3][0], bingoSheet[4][0]]
        bingoCol1 = [bingoSheet[0][1], bingoSheet[1][1], bingoSheet[2][1], bingoSheet[3][1], bingoSheet[4][1]]
        bingoCol2 = [bingoSheet[0][2], bingoSheet[1][2], bingoSheet[2][2], bingoSheet[3][2], bingoSheet[4][2]]
        bingoCol3 = [bingoSheet[0][3], bingoSheet[1][3], bingoSheet[2][3], bingoSheet[3][3], bingoSheet[4][3]]
        bingoCol4 = [bingoSheet[0][4], bingoSheet[1][4], bingoSheet[2][4], bingoSheet[3][4], bingoSheet[4][4]]
        if (bingoSheet[0] == marked or 
            bingoSheet[1] == marked or 
            bingoSheet[2] == marked or 
            bingoSheet[3] == marked or 
            bingoSheet[4] == marked or
            bingoCol0 == marked or
            bingoCol1 == marked or
            bingoCol2 == marked or
            bingoCol3 == marked or
            bingoCol4 == marked ):
            winningSheet = bingoSheet
            winningNumber = int(num)
            break
    if winningNumber is not None:
        break

# calculate which board wins first
sum = 0
for bingoRow in winningSheet:
    for bingoNumber in bingoRow:
        if bingoNumber != 'X':
            sum += int(bingoNumber)

print(sum * winningNumber)