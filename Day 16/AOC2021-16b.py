# Advent of Code 2021 Day 16 - Part 1
import sys
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

def resultType(typeId):
    resultDict = {
        0: 0,
        1: 1,
        2: sys.maxsize,
        3: -1,
        5: '>',
        6: '<',
        7: '='
    }
    return resultDict[typeId]

class Packet:
    def __init__(self,version,typeId):
        self.version = version
        self.typeId = typeId
        self.subPacketData = []
        self.literalVal = -1
    def append(self,packet):
        self.subPacketData.append(packet)
    def setLiteralVal(self,val):
        self.literalVal = val

def processPacketData(data):
    if len(data) < 3:
        return (None,data)
    if int(data,2) == 0:
        return (None,data)
    version = int(data[0:3],2)
    typeId = int(data[3:6],2)
    packet = Packet(version,typeId)
    if typeId == 4:
        packetData = data[6:]
        literalVal = ''
        for i in range(0,len(packetData),5):
            literalValData = packetData[i:i+5]
            flag = int(literalValData[0])
            literalVal += literalValData[1:]
            if flag == 0:
                break
        packet.setLiteralVal(int(literalVal,2))
        subPacketData = packetData[i+5:]
        return (packet,subPacketData)
    else:
        lengthTypeId = int(data[6],2)
        if lengthTypeId == 0:
            totalSubPacketLength = int(data[7:22],2)
            subPacketData = data[22:22+totalSubPacketLength]
            while subPacketData != '':
                packetTuple = processPacketData(subPacketData)
                packet.append(packetTuple[0])
                subPacketData = packetTuple[1]
            return (packet,data[22+totalSubPacketLength:])
        elif lengthTypeId == 1:
            subPacketNo = int(data[7:18],2)
            subPacketData = data[18:]
            for j in range(subPacketNo):
                packetTuple = processPacketData(subPacketData)
                packet.append(packetTuple[0])
                subPacketData = packetTuple[1]
            return (packet,subPacketData)
    return (packet,subPacketData)

def processPacket(packet):
    if packet.typeId == 4:
        return packet.literalVal
    else:
        result = resultType(packet.typeId)
        if packet.typeId < 4:
            for p in packet.subPacketData:
                if packet.typeId == 0:
                    result += processPacket(p)
                elif packet.typeId == 1:
                    result *= processPacket(p)
                elif packet.typeId == 2:
                    result = min(result,processPacket(p))
                elif packet.typeId == 3:
                    result = max(result,processPacket(p))
        elif packet.typeId == 5:
            result = 1 if processPacket(packet.subPacketData[0]) > processPacket(packet.subPacketData[1]) else 0
        elif packet.typeId == 6:
            result = 1 if processPacket(packet.subPacketData[0]) < processPacket(packet.subPacketData[1]) else 0
        elif packet.typeId == 7:
            result = 1 if processPacket(packet.subPacketData[0]) == processPacket(packet.subPacketData[1]) else 0
        return result

f = open('input.txt', 'r')
data = f.readlines()
data = list(map(processData, data))
f.close()

bitString = ''
for string in data:
    for c in string:
        bitString += convertToBinary(c)
packet = processPacketData(bitString)[0]
answer = processPacket(packet)
print(answer)
