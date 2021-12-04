# Advent of Code 2021 Day 1 Part A
def replaceAndConvert(num):
    num = num.replace('\n', '')
    return int(num)

f = open('input.txt', 'r')
items = f.readlines()
items = list(map(replaceAndConvert, items))
f.close()
count = 0
maxNum = items[0] + items[1] + items[2]
for i in range(1,len(items)-2):
    sum = items[i] + items[i+1] + items[i+2]
    if maxNum < sum:
        count += 1
    maxNum = sum
print(count)    