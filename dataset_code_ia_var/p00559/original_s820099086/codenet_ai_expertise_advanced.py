from sys import stdin
from functools import partial

N, Q, S, T = map(int, stdin.readline().split())
A = [int(stdin.readline()) for _ in range(N + 1)]
diff = [a2 - a1 for a1, a2 in zip(A, A[1:])]

calc = lambda v: -S * v if v > 0 else -T * v

ret = sum(map(calc, diff))

for _ in range(Q):
    a, b, c = map(int, stdin.readline().split())
    a1 = a - 1
    updated = []
    for idx, delta in ((a1, c), (b, -c)):
        if 0 <= idx < N:
            ret -= calc(diff[idx])
            diff[idx] += delta
            ret += calc(diff[idx])
    print(ret)