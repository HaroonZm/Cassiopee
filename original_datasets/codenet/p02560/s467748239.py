def floor_sum(n, m, a, b):
    res = 0
    while True:
        if a >= m:
            res += a//m * n * (n-1) // 2
            a %= m
        if b >= m:
            res += b//m * n
            b %= m
        Y = (a*n+b) // m
        X = Y*m-b
        if Y == 0:
            return res
        res += (n-(X+a-1)//a) * Y
        n, m, a, b = Y, a, m, -X%a

import sys
input = sys.stdin.buffer.readline
t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))