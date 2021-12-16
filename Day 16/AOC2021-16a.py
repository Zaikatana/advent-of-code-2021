# Advent of Code 2021 Day 16 - Part 1
def processData(string):
    string = string.replace('\n','')
    return string

def convertToBinary(char):
    binaryDict = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111',
    }
    return binaryDict[char]

def processPacketData(data):
    if len(data) < 3:
        return 0
    if int(data,2) == 0:
        return 0
    version = int(data[0:3],2)
    typeId = int(data[3:6],2)
    totalVersion = version
    if typeId == 4:
        packetData = data[6:]
        literalVal = ''
        for i in range(0,len(packetData),5):
            literalValData = packetData[i:i+5]
            flag = int(literalValData[0])
            literalVal += literalValData[1:]
            if flag == 0:
                break
        subPacketData = packetData[i+5:]
    else:
        lengthTypeId = int(data[6],2)
        if lengthTypeId == 0:
            totalSubPacketLength = int(data[7:22],2)
            subPacketData = data[22:]
        elif lengthTypeId == 1:
            subPacketNo = int(data[7:18],2)
            subPacketData = data[18:]
    totalVersion += processPacketData(subPacketData)
    return totalVersion

f = open('input.txt', 'r')
data = f.readlines()
data = list(map(processData, data))
f.close()

bitString = ''
for string in data:
    for c in string:
        bitString += convertToBinary(c)

answer = processPacketData(bitString)
print(answer)
