import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)

J = 0
O = 1
I = 2
JO = 3
OI = 4

num_JOI = 0

N = int(input())
input_str = input()

dp = [[0]*(5) for _ in range(N+1)]

for i in range(1,(N+1)):
    if input_str[i-1] == "J":
        dp[i][J] += 1
    elif input_str[i-1] == "O":
        dp[i][O] += 1
        dp[i][JO] += dp[i-1][J]
    else: #input_str[i-1] == "I"
        dp[i][I] += 1
        dp[i][OI] += dp[i-1][O]
        num_JOI += dp[i-1][JO]
    for k in range(5):
        dp[i][k] += dp[i-1][k] #累積和にする

maximum = max(dp[N][JO],dp[N][OI]) #右端にIを足した場合と、左端にJを足した場合の大きい方

#最大の加算をもたらすOを探す
for i in range(1,(N+1)):
    if input_str[i-1] == "J":
        maximum = max(maximum,dp[i][J]*(dp[N][I]-dp[i][I]))
    elif input_str[i-1] == "O":
        maximum = max(maximum,dp[i-1][J]*(dp[N][I]-dp[i][I]))
    else:
        maximum = max(maximum,dp[i-1][J]*(dp[N][I]-dp[i][I]+1))

print("%d"%(num_JOI+maximum))