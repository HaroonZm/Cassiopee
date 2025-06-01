N = int(input())
A = list(map(int, input().split()))
from bisect import bisect_left

A.sort()
for n in range(N, 0, -1):
    if len(A) - bisect_left(A, n) >= n:
        print(n)
        break