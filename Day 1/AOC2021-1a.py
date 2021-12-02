# Advent of Code 2021 Day 1 Part A
def replaceAndConvert(num):
    num = num.replace('\n', '')
    return int(num)

f = open('input.txt', 'r')
items = f.readlines()
items = map(replaceAndConvert, items)
f.close()
count = 0
for i in range(1,len(items)):
    if items[i] > items[i-1]:
        count += 1

print count