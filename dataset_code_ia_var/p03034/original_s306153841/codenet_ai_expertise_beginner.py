import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
N = N - 1
ans = 0

for d in range(1, N + 1):
    a = N - d
    res = 0
    p = N
    q = 0
    while a >= d:
        if a <= N - a and N % d == 0:
            break
        p = p - d
        q = q + d
        res = res + S[p] + S[q]
        if res > ans:
            ans = res
        a = a - d

print(ans)