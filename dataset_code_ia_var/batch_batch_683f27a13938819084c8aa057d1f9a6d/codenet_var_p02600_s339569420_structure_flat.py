import sys, re
from decimal import *
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, floor, trunc, log
from heapq import heappush, heappop, heapify, nlargest, nsmallest
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

x = int(input())
if x >= 400 and x <= 599:
    print(8)
else:
    if x >= 600 and x <= 799:
        print(7)
    else:
        if x >= 800 and x <= 999:
            print(6)
        else:
            if x >= 1000 and x <= 1199:
                print(5)
            else:
                if x >= 1200 and x <= 1399:
                    print(4)
                else:
                    if x >= 1400 and x <= 1599:
                        print(3)
                    else:
                        if x >= 1600 and x <= 1799:
                            print(2)
                        else:
                            print(1)