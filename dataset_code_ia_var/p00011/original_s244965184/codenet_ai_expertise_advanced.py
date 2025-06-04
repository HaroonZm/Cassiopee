import sys
from itertools import islice

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
swaps = [tuple(map(int, line.rstrip().split(','))) for line in islice(sys.stdin, m)]

transitions = [{} for _ in range(m)]
for idx, (a, b) in enumerate(swaps):
    transitions[idx][a], transitions[idx][b] = b, a

for start in range(1, n + 1):
    pos = start
    for t in reversed(transitions):
        pos = t.get(pos, pos)
    print(pos)