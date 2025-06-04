from sys import stdin
from functools import reduce
from operator import mul

N = int(stdin.readline())
T = list(map(int, stdin.readline().split()))
A = list(map(int, stdin.readline().split()))

H = [0] * N
flag = False

H[0] = T[0]
for i in range(1, N):
    H[i] = T[i] if T[i] != T[i - 1] else -T[i]

H[-1] = A[-1]

for i in range(1, N):
    idx = N - i - 1
    if A[idx] != A[idx + 1]:
        check = (-H[idx] if H[idx] < 0 else H[idx])
        if A[idx] > check:
            flag = True
            break
        H[idx] = A[idx]
    else:
        H[idx] = max(-A[idx], H[idx])

if N == 1:
    print(1 if A[0] == T[0] else 0)
elif not flag:
    MOD = 10**9 + 7
    negatives = [-h for h in H if h < 0]
    res = reduce(lambda x, y: x * y % MOD, negatives, 1) if negatives else 1
    print(res)
else:
    print(0)