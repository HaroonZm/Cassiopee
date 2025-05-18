# Template 1.0
import sys, re
from decimal import *
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, floor, trunc, log
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

x = INT()

if(x>=400 and x<=599):
    print(8)
elif(x>=600 and x<=799):
    print(7)
elif(x>=800 and x<=999):
    print(6)
elif(x>=1000 and x<=1199):
    print(5)
elif(x>=1200 and x<=1399):
    print(4)
elif(x>=1400 and x<=1599):
    print(3)
elif(x>=1600 and x<=1799):
    print(2)
else:
    print(1)