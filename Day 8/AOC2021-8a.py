# Advent of Code 2021 Day 8 - Part 1
def removeNewLine(string):
    string = string.replace('\n','')
    signalLines = string.split(' | ')
    return signalLines

f = open('input.txt', 'r')
signalLines = f.readlines()
signalLines = list(map(removeNewLine, signalLines))
signalLines = signalLines
f.close()

answer = 0
for line in signalLines:
    fourDigitDisplay = line[1].split(' ')
    # check if digits are of length 2,3,4,7 (1,7,4,8)
    for digit in fourDigitDisplay:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            answer += 1

print(answer)
