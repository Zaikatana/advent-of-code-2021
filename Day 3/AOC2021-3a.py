# Advent of Code 2021 Day 3 - Part 1
def removeNewLine(string):
    return string.replace('\n','')

f = open('input.txt', 'r')
diagnostic = f.readlines()
diagnosticCount = len(diagnostic)
diagnostic = map(removeNewLine, diagnostic)
f.close()
diagnosticLength = len(diagnostic[0])
diagnosticOneCount = []
gamma = ''
epsilon = ''

# figure way to do it without o(n^2)
# calculate amount of ones per line
for i in range(0,diagnosticLength):
    oneCount = 0
    for d in diagnostic:
        if d[i] == '1':
            oneCount += 1
    diagnosticOneCount.append(oneCount)

diagnosticZeroCount = []

# calculate amount of zeroes per line
for ones in diagnosticOneCount:
    diagnosticZeroCount.append(diagnosticCount - ones)


# generate gamma
for j in range(0, len(diagnosticOneCount)):
    if diagnosticOneCount[j] > diagnosticZeroCount[j]:
        gamma += '1'
    else:
        gamma += '0'

# generate epsilon
for k in range(0, len(gamma)):
    if gamma[k] == '1':
        epsilon += '0'
    else:
        epsilon += '1'

# convert binary to integer
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print gamma * epsilon
