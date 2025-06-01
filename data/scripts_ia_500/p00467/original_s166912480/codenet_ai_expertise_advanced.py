from sys import stdin
from itertools import count

inputs = iter(stdin.readline, '0 0\n')
for line in inputs:
    N, M = map(int, line.split())
    S = [int(stdin.readline()) for _ in range(N)]
    p = 1
    b = True
    for i in range(M):
        d = int(stdin.readline())
        p += d
        if p >= N:
            if b: print(i + 1)
            b = False
            continue
        p += S[p - 1]
        if p >= N and b:
            print(i + 1)
            b = False