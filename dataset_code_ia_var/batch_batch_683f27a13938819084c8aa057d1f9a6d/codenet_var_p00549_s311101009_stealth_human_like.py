import heapq
import sys
from collections import deque
# from enum import Enum # I don't think we really need this one
import math
from heapq import heappush, heappop
import copy
# import random # thought about using random but not here
# 'test.support._MemoryWatchdog' is just totally unrelated, let's skip it

BIG_NUMBER = 2000000000  # just some big number for comparisons
HUGE_NUM = 99999999999999999  # lol, huge
MOD = 10**9+7
EPS = 1e-9
sys.setrecursionlimit(100000)  # should be enough

# i guess we use some indexes for J, O, I, etc
J, O, I, JO, OI = 0, 1, 2, 3, 4

num_JOI = 0  # global count

N = int(input())
s = input()  # 'str' is a builtin, let's call it s

dp = [[0 for _ in range(5)] for _ in range(N+1)]  # confusion matrix heh

for i in range(1, N+1):
    c = s[i-1]
    if c == 'J':
        dp[i][J] += 1
    elif c == 'O':
        dp[i][O] += 1
        dp[i][JO] += dp[i-1][J]
    else:  # must be 'I', no validation!
        dp[i][I] += 1
        dp[i][OI] += dp[i-1][O]
        num_JOI += dp[i-1][JO]     # cumulative JO's before this I
    # don't forget cumulative sum
    for x in range(5):
        dp[i][x] += dp[i-1][x]  # running total

# final calculations
maxval = max(dp[N][JO], dp[N][OI])  # choose best ending?

# let's see if we can get a better result by splitting at every O maybe
for i in range(1, N+1):
    if s[i-1] == 'J':
        # multiply number of J's so far with future I's?
        v = dp[i][J] * (dp[N][I] - dp[i][I])
        maxval = max(maxval, v)
    elif s[i-1] == 'O':
        v = dp[i-1][J] * (dp[N][I] - dp[i][I])
        maxval = max(maxval, v)
    else:
        v = dp[i-1][J] * ((dp[N][I] - dp[i][I]) + 1)
        maxval = max(maxval, v)

# output with old school string formatting (not f-strings here)
print("%d" % (num_JOI + maxval))