import itertools
import sys
import math
from functools import lru_cache
from queue import Queue
from operator import mul
from functools import reduce

input = sys.stdin.readline

x, y, z, kk = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

ll = []
for i in range(len(a)):
    for j in range(len(b)):
        if i * j > kk:
            break
        for k in range(len(c)):
            if i * j * k > kk:
                break
            ll.append(a[i] + b[j] + c[k])
ll.sort(reverse=True)

for i in range(kk):
    print(ll[i])