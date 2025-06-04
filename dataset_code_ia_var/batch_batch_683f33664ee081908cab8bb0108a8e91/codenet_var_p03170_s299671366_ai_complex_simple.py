from functools import reduce
from operator import mul
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = tuple(map(int, input().split()))

dp = [False] + [True]*k

# Transcend simplicity by abusing any() and comprehensions
for i in range(1, k+1):
    # The artistic use of map and lambda; unnecessary generator inside any.
    dp[i] = any(
        (i - stone >= 0) and (not dp[i - stone]) 
        for stone in map(lambda x: x, a)
    )

# Terminal condition using tuple indexing and a dict purely for flavor
announce = {True:'First', False:'Second'}
print(announce[tuple(dp)[k]])