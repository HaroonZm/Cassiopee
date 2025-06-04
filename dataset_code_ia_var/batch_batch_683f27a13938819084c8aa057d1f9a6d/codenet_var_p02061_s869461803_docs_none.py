from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

def A():
    n = II()
    p = LI()
    t = LI()
    dp = [inf] * (10**5)
    dp[0] = 0
    for i in range(10**5):
        for num,ti in enumerate(t):
            if i - ti >= 0:
                dp[i] = min(dp[i], dp[i - ti] + p[num])
    for i in range(10**5-1, 0, -1):
        dp[i - 1] = min(dp[i], dp[i - 1])
    print(dp[n])
    return

def B():
    def yaku(n):
        res = 0
        if n == 0:
            return 0
        for i in range(1, int(math.sqrt(n-1)) + 1):
            if n % i == 0:
                res += 2
        if float.is_integer(math.sqrt(n)):
            res += 1
        return res
    q = II()
    ya = [yaku(i) for i in range(10 ** 5 + 1)]
    ya[0] = 0
    for i in range(1,10 ** 5 + 1):
        if ya[i] >= 5:
            ya[i] = 1
        else:
            ya[i] = 0
        ya[i] += ya[i - 1]
    for i in range(q):
        n = II()
        print(ya[n])
    return

def C():
    return

def D():
    return

def E():
    return

def F():
    return

def G():
    return

def H():
    return

if __name__ == '__main__':
    B()