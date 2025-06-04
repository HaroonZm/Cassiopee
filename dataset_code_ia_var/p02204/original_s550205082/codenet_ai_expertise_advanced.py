import sys
from itertools import groupby

input = sys.stdin.readline

M, N = map(int, input().split())
A = list(map(int, input().split()))

if M == 2:
    parities = [(a % 2) == (i % 2) for i, a in enumerate(A)]
    res = min(sum(parities), N - sum(parities))
    print(res)
else:
    A.append(10**10)
    ANS = sum(len(list(group)) // 2 for _, group in groupby(A))
    print(ANS)