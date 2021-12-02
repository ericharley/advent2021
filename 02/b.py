import re

with open('input.txt') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

p = re.compile(r'(?P<direction>(forward)|(up)|(down)) (?P<length>[0-9]+)')

for line in lines:

    m = p.search(line)
    direction = m.group('direction')
    length = int(m.group('length'))

    if direction == 'forward':
       horizontal += length
       depth += aim*length

    if direction == 'up':
       aim -= length

    if direction == 'down':
       aim += length

print(f'{depth}*{horizontal} = {depth*horizontal}')
