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
    """
    6 7
6 8
6 9
6 10
6 13
6 14
6 15
6 19
6 20
6 25
    """
    A, B = mi()
    if B > (A - 1) ** 2:
        print(-1)
        sys.exit()
    if B % (A - 1) == 0:
        print(A * ceil(B / A))
    else:
        a = B // (A - 1)
        b = B % (A - 1)
        if a < b:
            print(A * ceil(B / A))
        else:
            print(-1)
    # dp1 = [float('inf')] * 100
    # dp2 = [float('inf')] * 100
    # dp1[0] = dp2[0] = 0
    # for i in range(1, 100):
    #     dp1[i] = min(dp1[i], dp1[i - 1] + 1)
    #     if i >= A:
    #         dp1[i] = min(dp1[i], dp1[i - A] + 1)
    #     if i >= B:
    #         dp1[i] = min(dp1[i], dp1[i - B] + 1)
    # for i in range(1, 100):
    #     if i >= B:
    #         dp2[i] = dp2[i - B] + 1
    #     elif i >= A:
    #         dp2[i] = dp2[i - A] + 1
    #     else:
    #         dp2[i] = dp2[i - 1] + 1
    # for i in range(100):
    #     if dp1[i] != dp2[i]:
    #         print(A, B)
    #         break
    # for i in range(100):
    #     if dp1[i] != dp2[i]:
    #         debug(i, dp1[i], dp2[i], "?")

if __name__ == '__main__':
    main()