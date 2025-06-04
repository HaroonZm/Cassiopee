import sys, math
from decimal import Decimal as D
from collections import Counter as C, deque as dq
from copy import deepcopy as dc
sys.setrecursionlimit(10**9)
MODULO = 10 ** 9 + 7

get = lambda: input()
to_int = lambda: int(input())
split_str = input
parse = lambda: (int(x) for x in input().split())
lst = lambda: list(map(int, input().split()))
def LCM(x, y):
    return math.gcd(x, y) and x * y // math.gcd(x, y) or 0

for _ in range(1):
    n = to_int()
    print(['ABC','ABD'][n>=1000])