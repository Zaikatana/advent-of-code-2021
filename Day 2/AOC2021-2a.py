# Advent of Code Day 2 Part 1
def replaceAndConvert(cmd):
    cmd = cmd.replace('\n', '')
    return cmd

f = open('input.txt', 'r')
commands = f.readlines()
commands = map(replaceAndConvert, commands)
depth = 0
horizontal = 0

for command in commands:
    command = command.split(' ')
    direction = command[0]
    distance = int(command[1])
    if direction == 'up':
        depth -= distance
    elif direction == 'down':
        depth += distance
    elif direction == 'forward':
        horizontal += distance

print(horizontal * depth)

