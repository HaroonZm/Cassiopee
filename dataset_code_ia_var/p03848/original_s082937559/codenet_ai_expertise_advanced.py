from sys import stdin
from functools import reduce

MOD = 10**9 + 7
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
A.sort(reverse=True)

expected = (
    [i for i in range(2, N, 2)] * 2 + [0] if N % 2 else [i for i in range(1, N, 2)] * 2
)
expected.sort(reverse=True)

ans = pow(2, N // 2, MOD) if A == expected else 0

print(ans)