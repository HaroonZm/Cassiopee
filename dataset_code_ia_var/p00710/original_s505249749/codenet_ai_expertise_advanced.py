from sys import stdin
from itertools import islice

def process(seq, ops):
    for p, c in ops:
        p -= 1
        l1 = seq[p:p+c]
        l2 = seq[:p]
        seq[:p+c] = l1 + l2
    return seq[0]

lines = iter(stdin.read().splitlines())
while True:
    n, r = map(int, next(lines).split())
    if n == 0 and r == 0:
        break
    seq = list(range(n, 0, -1))
    ops = [tuple(map(int, next(lines).split())) for _ in range(r)]
    print(process(seq, ops))