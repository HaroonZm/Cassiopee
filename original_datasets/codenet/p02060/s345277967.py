import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy
from collections import Counter, deque
import heapq
from functools import reduce
# local only
# if not __debug__:
#     fin = open('in_1.txt', 'r')
#     sys.stdin = fin
# local only
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

def main():
    N = ii()
    p = lmi()
    t = lmi()
    n = len(p)
    v = [(i, p[i] / t[i]) for i in range(n)]
    v.sort(key=itemgetter(1))
    m = v[0][0]
    # print(v)
    ans = ceil(N / t[m]) * p[m]
    for i in range(4):
        if i != m:
            # print(ceil((N - t[i]) // t[m]))
            ans = min(ans, ceil((N - t[i]) / t[m]) * p[m] + p[i])
            # print(ans)
    print(ans)

if __name__ == '__main__':
    main()