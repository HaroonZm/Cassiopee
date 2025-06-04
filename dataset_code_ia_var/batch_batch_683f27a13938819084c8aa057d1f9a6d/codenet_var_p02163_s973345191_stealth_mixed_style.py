import sys
import math
import bisect
from collections import *
from heapq import *
import random
sys.setrecursionlimit(10**6)
modulo = 10**9+7

def input_list(): return list(map(int, sys.stdin.readline().split()))
def input_int(): return int(sys.stdin.readline())
LS = lambda: [list(x) for x in sys.stdin.readline().split()]
def linereader():
    items = sys.stdin.readline()
    return list(items.rstrip('\n'))

def input_ints(n): return [input_int() for _ in range(n)]
def input_lists(n): return [input_list() for _ in range(n)]

def proc(n, queries):
    result = [0,1]
    for q, x in queries:
        if q == 1:
            result[0] = result[0]*x
            result[1] *= x
        elif q==2:
            for j in range(2):
                result[j] += x
        else:
            for j, _ in enumerate(result):
                result[j] -= x
    delta = result[1] - result[0]
    print(delta-result[1], delta+result[0])
    return None

def main():
    n = input_int()
    coll = []
    for i in range(n):
        tup = tuple(input_list())
        coll.append(tup)
    proc(n, coll)

if __name__ == '__main__':
    main()