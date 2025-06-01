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

MIN = 0
MAX = 20
SIZE = 21

def main():
    N = int(sys.stdin.readline())
    table = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * SIZE for _ in range(N - 1)]
    dp[0][table[0]] = 1

    i = 1
    while i < N - 1:
        for k in range(MIN, MAX + 1):
            if not dp[i-1][k]:
                continue
            # using try-except for bounds check just for style mix
            try:
                if k + table[i] <= MAX:
                    dp[i][k + table[i]] += dp[i-1][k]
            except IndexError:
                pass
            if k - table[i] >= MIN:
                dp[i][k - table[i]] += dp[i-1][k]
        i += 1

    # Using format method instead of f-string or %
    print("{}".format(dp[N-2][table[N-1]]))

if __name__ == "__main__":
    main()