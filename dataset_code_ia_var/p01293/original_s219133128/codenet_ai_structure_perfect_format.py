#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt

def LI():
    return list(map(int, input().split()))

def LF():
    return list(map(float, input().split()))

def LI_():
    return list(map(lambda x: int(x) - 1, input().split()))

def II():
    return int(input())

def IF():
    return float(input())

def LS():
    return list(map(list, input().split()))

def S():
    return list(input().rstrip())

def IR(n):
    return [II() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def FR(n):
    return [IF() for _ in range(n)]

def LFR(n):
    return [LI() for _ in range(n)]

def LIR_(n):
    return [LI_() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

mod = 1000000007
inf = 1e10

def solve():
    n = input().rstrip()
    if n == "#":
        return False
    lis = [LS() for _ in range(4)]
    num = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    ans = [0] * 4
    master = 0
    for i in range(13):
        north = lis[0][i]
        east = lis[1][i]
        south = lis[2][i]
        west = lis[3][i]
        suit = [north[1], east[1], south[1], west[1]]
        tmp = [num.index(lis[master][i][0]), master]
        if n in suit:
            tmp = [-1, -1]
            for k in range(4):
                if suit[k] == n:
                    if tmp[0] < num.index(lis[k][i][0]):
                        tmp = [num.index(lis[k][i][0]), k]
        else:
            for k in range(4):
                if suit[tmp[1]] == suit[k] and tmp[0] < num.index(lis[k][i][0]):
                    tmp = [num.index(lis[k][i][0]), k]
        ans[tmp[1]] += 1
        master = tmp[1]
    a = ans[0] + ans[2] - 6
    b = ans[1] + ans[3] - 6
    if a > b:
        print("NS {}".format(a))
    else:
        print("EW {}".format(b))
    return True

if __name__ == '__main__':
    while solve():
        pass