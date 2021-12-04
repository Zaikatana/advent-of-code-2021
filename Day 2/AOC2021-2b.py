# Advent of Code Day 2 Part 2
def replaceAndConvert(cmd):
    cmd = cmd.replace('\n', '')
    return cmd

f = open('input.txt', 'r')
commands = f.readlines()
commands = list(map(replaceAndConvert, commands))
depth = 0
horizontal = 0
aim = 0

for command in commands:
    command = command.split(' ')
    direction = command[0]
    distance = int(command[1])
    if direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
    elif direction == 'forward':
        horizontal += distance
        depth += (aim * distance)

print(horizontal * depth)
