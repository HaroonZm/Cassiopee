from sys import stdin
from itertools import takewhile

for line in takewhile(lambda l: not l.startswith('#'), stdin):
    name, day, num, *rest = line.strip().split()
    day, num = int(day), int(num)
    if (day == 31 and num >= 5) or day >= 32:
        name = '?'
        day -= 30
    print(' '.join(map(str, (name, day, num, *rest))))