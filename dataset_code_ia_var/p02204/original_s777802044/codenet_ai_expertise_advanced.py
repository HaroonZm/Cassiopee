from sys import stdin
from itertools import starmap

M, N = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

if M == 2:
    parity = [i % 2 == v % 2 for i, v in enumerate(A)]
    count = sum(parity)
    print(min(count, N - count))
else:
    ret = sum(A[i] == A[i - 1] for i in range(1, N))
    from itertools import groupby
    print(ret)