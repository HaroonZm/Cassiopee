from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N = input()
c = map(int, raw_input().split())
num = [0] * N
Q = input()
for i in range(Q):
    t, x, d = map(int, raw_input().split())
    if t == 1:
        num[x - 1] += d
    else:
        num[x - 1] -= d
    if not 0 <= num[x - 1] <= c[x - 1]:
        print x
        exit()
print 0