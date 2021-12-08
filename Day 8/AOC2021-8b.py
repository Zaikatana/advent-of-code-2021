# Advent of Code 2021 Day 8 - Part 2
import re

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
    one = ''
    seven = ''
    four = ''
    eight = ''
    segmentDict = {}
    numDict = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9'
    }
    # array to store strings of length 5
    fives = []
    tenDigitDisplay = line[0].split(' ')
    fourDigitDisplay = line[1].split(' ')

    # retrieve string combinations for 1, 7, 4 and 8
    for digit in tenDigitDisplay:
        if len(digit) == 2:
            one = digit
        elif len(digit) == 3:
            seven = digit
        elif len(digit) == 4:
            four = digit
        elif len(digit) == 7: 
            eight = digit
        elif len(digit) == 5:
            fives.append(digit)

    # Essentially the idea is to figure out the position of the segments and map them to a-g
    # Letter at Pos a
    segmentDict['a'] = re.sub(f'[{one}]','',seven)
    # Letter at Pos g
    for five in fives:
        regex = ''.join(set(four+seven))
        affected = re.sub(f'[{regex}]','',five)
        if len(affected) == 1:
            segmentDict['g'] = affected
            break
    # Letter at Pos d
    for five in fives:
        regex = ''.join(set(segmentDict['a']+one+segmentDict['g']))
        affected = re.sub(f'[{regex}]','',five)
        if len(affected) == 1:
            segmentDict['d'] = affected
            break
    # Letter at Pos b
    seg = ''.join(set(one+segmentDict['d']))
    segmentDict['b'] = re.sub(f'[{seg}]','',four)
    # Letter at Pos f
    for five in fives:
        regex = ''.join(set(segmentDict['a']+segmentDict['b']+segmentDict['d']+segmentDict['g']))
        affected = re.sub(f'[{regex}]','',five)
        if len(affected) == 1:
            segmentDict['f'] = affected
            break
    # Letter at Pos c
    segmentDict['c'] = one.replace(segmentDict['f'],'')
    # Letter at Pos e
    seg = segmentDict['a']+segmentDict['b']+segmentDict['c']+segmentDict['d']+segmentDict['f']+segmentDict['g']
    segmentDict['e'] = re.sub(f'[{seg}]','',eight)
    # reverse map to get updated mapping
    segmentDict = {v: k for k, v in segmentDict.items()}
    finalDigit = ''
    # figure out digit identity and then append to string, then add result to answer
    for digit in fourDigitDisplay:
        digitString = ''
        for c in digit:
            digitString += str(segmentDict[c])
        digitString = ''.join(sorted(digitString))
        digitNum = numDict[digitString]
        finalDigit += digitNum
    answer += int(finalDigit)
        
print(answer)
