# Advent of Code 2021 Day 10 - Part 2
import math

def processData(string):
    string = string.replace('\n','')
    return string

f = open('input.txt', 'r')
ssLine = f.readlines()
ssLine = list(map(processData, ssLine))
f.close()

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
leftOvers = []

# Load opening braces into a stack, if a closing brace is encountered, pop the brace and validate whether it is a matching brace
for line in ssLine:
    stack = []
    hasErrors = False
    for brace in line:
        if brace == '(' or brace == '[' or brace == '{' or brace == '<':
            stack.append(brace)
        else:
            poppedBrace = stack.pop()
            if brace == ')':
                if poppedBrace != '(':
                    hasErrors = True
            elif brace == ']':
                if poppedBrace != '[':
                    hasErrors = True
            elif brace == '}':
                if poppedBrace != '{':
                    hasErrors = True
            else:
                if poppedBrace != '<':
                    hasErrors = True
    # If there are no errors then what's remaining in the stack is what needs to be considered
    if hasErrors is False:
        leftOvers.append(list(reversed(stack)))

# Calculate all scores
scores = []
for lo in leftOvers:
    score = 0
    for brace in lo:
        score *= 5
        score += points[brace]
    scores.append(score)

# Calculate the middle score
scores = sorted(scores)
answer = scores[math.floor(len(scores)/2)]
print(answer)
