# Advent of Code 2021 Day 10 - Part 1
def processData(string):
    string = string.replace('\n','')
    return string

f = open('input.txt', 'r')
ssLine = f.readlines()
ssLine = list(map(processData, ssLine))
f.close()

answer = 0
stack = []
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

for line in ssLine:
    for brace in line:
        if brace == '(' or brace == '[' or brace == '{' or brace == '<':
            stack.append(brace)
        else:
            poppedBrace = stack.pop()
            if brace == ')':
                if poppedBrace != '(':
                    answer += points[')']
            elif brace == ']':
                if poppedBrace != '[':
                    answer += points[']']
            elif brace == '}':
                if poppedBrace != '{':
                    answer += points['}']
            else:
                if poppedBrace != '<':
                    answer += points['>']

print(answer)
