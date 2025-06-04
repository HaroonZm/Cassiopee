import sys
import math
from itertools import permutations
from collections import defaultdict

sys.setrecursionlimit(10**7)

def read():
    return sys.stdin.readline().rstrip()

def main():
    [a, b, k] = list(map(int, read().split()))

    def f(x, y, z):
        if z <= x:
            print(x-z, y)
        else:
            left = y-(z-x)
            y2 = left if left > 0 else 0
            print(0, y2)
    f(a, b, k)

main()