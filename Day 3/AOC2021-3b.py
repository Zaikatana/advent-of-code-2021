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

# figure way to do it without o(n^2)
# calculate amount of ones per line
for i in range(0,diagnosticLength):
    oneCount = 0
    for d in diagnostic:
        if d[i] == '1':
            oneCount += 1
    diagnosticOneCount.append(oneCount)

oxygenGeneratorRating = list(diagnostic)

for j in range(0,diagnosticLength):
    updatedList = []
    oneAmount = 0
    mostCommon = "1"
    for k in range(0, len(oxygenGeneratorRating)):
        if oxygenGeneratorRating[k][j] == "1":
            oneAmount += 1
    if oneAmount < len(oxygenGeneratorRating) - oneAmount:
        mostCommon = "0"
    for l in range(0, len(oxygenGeneratorRating)):
        if  oxygenGeneratorRating[l][j] == mostCommon:
            updatedList.append(oxygenGeneratorRating[l])
    oxygenGeneratorRating = updatedList
    if len(oxygenGeneratorRating) == 1:
        break
    
oxygenGeneratorRating = int(oxygenGeneratorRating[0], 2)

co2ScrubberRating = list(diagnostic)

for m in range(0,diagnosticLength):
    updatedList = []
    oneAmount = 0
    leastCommon = "0"
    for n in range(0, len(co2ScrubberRating)):
        if co2ScrubberRating[n][m] == "1":
            oneAmount += 1
    if oneAmount < len(co2ScrubberRating) - oneAmount:
        leastCommon = "1"
    for o in range(0, len(co2ScrubberRating)):
        if  co2ScrubberRating[o][m] == leastCommon:
            updatedList.append(co2ScrubberRating[o])
    co2ScrubberRating = updatedList
    if len(co2ScrubberRating) == 1:
        break
        
co2ScrubberRating = int(co2ScrubberRating[0], 2)

print oxygenGeneratorRating * co2ScrubberRating
