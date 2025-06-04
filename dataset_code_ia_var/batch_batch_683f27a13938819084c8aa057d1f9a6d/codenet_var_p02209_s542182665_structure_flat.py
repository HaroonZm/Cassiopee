from itertools import *
from bisect import *
from math import *
from collections import *
from heapq import *
from random import *
from decimal import *
import sys

sys.setrecursionlimit(10 ** 6)

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

n, k = map(int, sys.stdin.readline().split())
aa = list(map(int, sys.stdin.readline().split()))
bek = [False] * (1 << n)

bit = 0
while bit < (1 << n):
    if bek[bit] == False:
        s = 0
        for i, a in enumerate(aa):
            if (bit >> i) & 1:
                s += a
        if s == k:
            bek[bit] = True
        else:
            bit += 1
            continue
    j = 0
    while j < n:
        bek[bit | (1 << j)] = True
        j += 1
    bit += 1

mx = 0
bit = 0
while bit < (1 << n):
    if bek[bit]:
        bit += 1
        continue
    popcnt = bin(bit).count("1")
    if popcnt > mx:
        mx = popcnt
    bit += 1

print(n - mx)