import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy
from collections import Counter, deque
import heapq
from functools import reduce

sys.setrecursionlimit(200000)
input = sys.stdin.readline

def ii():
    return int(input())

def mi():
    return map(int, input().rstrip().split())

def lmi():
    return list(map(int, input().rstrip().split()))

def li():
    return list(input().rstrip())

def debug(*args, sep=" ", end="\n"):
    print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None

def exit(*arg):
    print(*arg)
    sys.exit()

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

if __name__ == '__main__':
    main()