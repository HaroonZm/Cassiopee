#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    s = S()
    f = [0,0]
    for i in s:
        if "A" <= i <= "M":
            f[0] += 1
        elif "N" <= i <= "Z":
            f[0] -= 1
        elif "a" <= i <= "m":
            f[1] += 1
        else:
            f[1] -= 1
    ans = []
    for i in s:
        if "A" <= i <= "M" and f[0] > 0:
            f[0] -= 1
            ans.append(i)
        elif "N" <= i <= "Z" and f[0] < 0:
            f[0] += 1
            ans.append(i)
        elif "a" <= i <= "m" and f[1] > 0:
            f[1] -= 1
            ans.append(i)
        elif "n" <= i <= "z" and f[1] < 0:
            f[1] += 1
            ans.append(i)
    print(len(ans))
    print(*ans,sep = "")
    return

if __name__ == "__main__":
    solve()