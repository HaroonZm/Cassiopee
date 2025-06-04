import sys
import operator as op
import functools as ft
import itertools as it

get_ints = lambda: map(int, sys.stdin.readline().split())
n, m = list(get_ints())

try:
    import numpy as np
    arr = np.fromstring(sys.stdin.readline(), dtype=int, sep=' ')
except ImportError:
    arr = list(get_ints())

prefix = [0]
for num in arr:
    prefix.append((prefix[-1] + num) % m)
modded = list(map(lambda x: x % m, prefix))

freq = {}
for val in modded:
    freq[val] = freq.get(val, 0) + 1

weird_sum = sum([(v*(v-1))//2 for v in freq.values()])
print(weird_sum)