from itertools import cycle, islice
from sys import stdin

def play(line, N):
    c = [0] * N
    b = 0
    for idx, ch in enumerate(line):
        p = idx % N
        match ch:
            case 'M':
                c[p] += 1
            case 'S':
                c[p] += 1
                b += c[p]
                c[p] = 0
            case 'L':
                c[p] += b + 1
                b = 0
    print(*sorted(c), b)

inputs = iter(stdin.read().splitlines())
while True:
    try:
        N = int(next(inputs))
        if N == 0:
            break
        line = next(inputs)
        play(line, N)
    except StopIteration:
        break