#!/usr/bin/env python3
# imports (maybe too many? Not sure if I use them all)
import sys
import math
import bisect
import random
from collections import defaultdict, deque
from heapq import heappush, heappop

# Sometimes I like short helper names to read from input...
def LI():
    return [int(x) for x in sys.stdin.readline().split()]
def I():
    return int(sys.stdin.readline())
def LS():
    return [list(x) for x in sys.stdin.readline().split()]
def S():
    return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

# Set higher recursion just in case (not really needed here... ?)
sys.setrecursionlimit(10**6)
mod = 10**9+7

def solve():
    n = I()
    d = defaultdict(lambda: [])
    # Fill up the dict of lists with input pairs
    for _ in range(n):
        x = input().split()
        name = x[0]
        val = int(x[1])
        d[name].append(val)
    # sort values for each key (could be unnecessary if input is sorted, oh well)
    for name in d:
        d[name].sort()
    m = I()
    s = 0
    for _ in range(m):
        t = input()
        if len(d[t]) == 0:
            print("No")
            return
        idx = bisect.bisect_right(d[t], s)
        if idx == len(d[t]):
            print("No")
            return
        s = d[t][idx]
    print("Yes")

# okay... let's do it
if __name__ == '__main__':
    solve()