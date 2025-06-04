from functools import reduce
import sys

for line in iter(sys.stdin.readline, ''):
    ints = list(map(int, line.strip()))
    if ints == [0]:
        break
    print(sum(ints))