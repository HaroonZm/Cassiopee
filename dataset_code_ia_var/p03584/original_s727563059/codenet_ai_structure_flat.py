from collections import Counter

import sys

data = list(map(int, sys.stdin.read().split()))
N = data[0]
K = data[1]
AB = data[2:]

C = Counter()
ab_iter = iter(AB)
while True:
    try:
        a = next(ab_iter)
        b = next(ab_iter)
        C[a] += b
    except StopIteration:
        break

ma = 0
for k, v in C.items():
    if k | K == K:
        ma += v

S = list(bin(K)[2:])
ones = 0
for ch in S:
    if ch == '1':
        ones += 1

i = -1
cnt = 0
while cnt < ones:
    T = S[:]
    idx = i + 1
    while T[idx] != '1':
        idx += 1
    i = idx
    for j in range(i + 1, len(T)):
        T[j] = '1'
    T[i] = '0'
    T_int = int("".join(T), 2)
    s = 0
    for k, v in C.items():
        if k | T_int == T_int:
            s += v
    if s > ma:
        ma = s
    cnt += 1

print(ma)