from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)
INF = 10 ** 18
MOD = 10 ** 9 + 7

N_K = raw_input().split()
N = int(N_K[0])
K = int(N_K[1])

if N <= 10:
    print 0
    sys.stdout.flush()
    for _ in range(K):
        for j in range(1, N + 1):
            print j
            sys.stdout.flush()
            if raw_input() == "Yes":
                break
    exit()

E = []
i = 0
while i < 8:
    E.append((1, i + 2))
    i += 1

v = 10
while v <= N:
    num = v - 10
    i = 0
    while i < 8:
        if num & (1 << i):
            E.append((v, i + 2))
        i += 1
    v += 1

print len(E)
idx = 0
while idx < len(E):
    u, v = E[idx]
    print u, v
    idx += 1

cnt = 0
while cnt < K:
    print 1
    sys.stdout.flush()
    S = raw_input()
    if S == "Yes":
        cnt += 1
        continue
    if S == "Near":
        i = 2
        found = False
        while i < 10:
            print i
            sys.stdout.flush()
            if raw_input() == "Yes":
                found = True
                break
            i += 1
        cnt += 1
        continue
    ans = 10
    i = 2
    while i < 10:
        print i
        sys.stdout.flush()
        s = raw_input()
        if s == "Near":
            ans += (1 << (i - 2))
        i += 1
    print ans
    sys.stdout.flush()
    S2 = raw_input()
    cnt += 1