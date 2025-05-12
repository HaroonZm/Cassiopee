import itertools
import math
import sys
import heapq
from collections import Counter
from collections import deque
from fractions import gcd
INF = 1 << 60
sys.setrecursionlimit(10 ** 6)

#ここから書き始める
n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
a = ""
for i in t:
    if i == "r":
        a += "p"
    elif i == "s":
        a += "r"
    else:
        a += "s"
ans = 0
for i in a:
    if i == "r":
        ans += r
    elif i == "s":
        ans += s
    else:
        ans += p
# print(ans)
for i in range(k, n):
    if a[i] == a[i - k]:
        if a[i] == "r":
            ans -= r
        elif a[i] == "s":
            ans -= s
        else:
            ans -= p
        a = a[:i] + "a" + a[i + 1:]
print(ans)